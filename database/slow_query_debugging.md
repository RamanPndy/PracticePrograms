A query like:

```sql
SELECT *
FROM orders
WHERE customer_id = 123
  AND status = 'active';
```

can be slow for several reasons. The **first thing I'd check is the execution plan** and indexes.

### 1. Missing composite index — most common reason

If you only have:

```sql
INDEX(customer_id)
```

the database may find all orders for customer `123`, then filter those rows by `status`.

A better index is often:

```sql
CREATE INDEX idx_orders_customer_status
ON orders(customer_id, status);
```

Now the database can directly locate:

```text
customer_id = 123
AND status = 'active'
```

instead of:

```text
Find all customer 123 orders
        ↓
Filter status
```

### 2. Why not just index `status`?

You could have:

```sql
INDEX(status)
```

but `status` is often **low cardinality**.

For example:

```text
active    → 70%
cancelled → 20%
completed → 10%
```

An index on `status` doesn't narrow the search much because a huge percentage of the table is `active`.

Compare:

```text
customer_id = 123
→ perhaps 500 rows

status = active
→ perhaps 70 million rows
```

So:

```sql
(customer_id, status)
```

is generally much more useful.

---

### 3. Column order matters

For this query:

```sql
WHERE customer_id = 123
  AND status = 'active'
```

I'd typically consider:

```sql
(customer_id, status)
```

rather than:

```sql
(status, customer_id)
```

because `customer_id` is usually much more selective.

For example:

```text
Index: (customer_id, status)

customer_id=123
       ↓
   small range
       ↓
status='active'
```

The optimal order ultimately depends on your workload, cardinality, and other queries.

---

### 4. `SELECT *` can make it slower

Suppose `orders` contains:

```text
id
customer_id
status
amount
address
shipping_address
billing_address
metadata JSON
payment_details JSON
...
```

You're asking the database to return **every column**.

If you only need:

```sql
SELECT id, amount
FROM orders
WHERE customer_id = 123
  AND status = 'active';
```

that's potentially much cheaper.

It can also allow a **covering index** in some databases.

For example:

```sql
CREATE INDEX idx_orders_customer_status_amount
ON orders(customer_id, status, amount);
```

The database may be able to answer the query directly from the index without reading the table rows.

---

### 5. Too many matching rows

Suppose:

```text
customer_id = 123
status = active
```

returns:

```text
5,000,000 rows
```

Even with a perfect index, the query can still be slow.

Why?

```text
Index lookup
     ↓
5 million matching rows
     ↓
Read rows
     ↓
Build result
     ↓
Send 5 million rows over network
```

An index doesn't make returning millions of rows cheap.

If you only need a page:

```sql
SELECT id, amount
FROM orders
WHERE customer_id = 123
  AND status = 'active'
ORDER BY id
LIMIT 50;
```

---

### 6. Stale statistics

The optimizer uses table/index statistics to decide how to execute the query.

If statistics are stale, it might estimate:

```text
Expected rows: 100
Actual rows: 5,000,000
```

and choose a bad execution plan.

For example, the optimizer might choose an index lookup when a sequential scan would actually be cheaper.

---

### 7. Data type mismatch

Suppose:

```sql
customer_id BIGINT
```

but the application sends something that causes an implicit conversion.

Depending on the database and query, implicit casts can interfere with index usage.

You want the predicate types to match the column type.

---

### 8. Function/cast on the indexed column

This can prevent efficient index usage.

For example, avoid patterns like:

```sql
WHERE CAST(customer_id AS TEXT) = '123'
```

or:

```sql
WHERE LOWER(status) = 'active'
```

unless you've specifically created an appropriate functional/expression index.

Prefer:

```sql
WHERE customer_id = 123
  AND status = 'active'
```

---

### 9. Index exists but isn't being used

This is where **`EXPLAIN` / `EXPLAIN ANALYZE`** becomes important.

For PostgreSQL:

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT *
FROM orders
WHERE customer_id = 123
  AND status = 'active';
```

You might see:

```text
Seq Scan on orders
  Filter: ((customer_id = 123) AND (status = 'active'))
```

That's a red flag if `orders` is large and the query is expected to be selective.

After adding:

```sql
CREATE INDEX idx_orders_customer_status
ON orders(customer_id, status);
```

you might see something like:

```text
Index Scan using idx_orders_customer_status
```

---

## Interview-style answer

If an interviewer asks:

> **"Why is this query slow?"**

I'd answer:

> First I'd check the execution plan using `EXPLAIN ANALYZE`. The likely issue is a missing or inappropriate index. Since the query filters on both `customer_id` and `status`, I'd consider a composite index on `(customer_id, status)`. I'd also check the number of rows returned, cardinality/selectivity, stale statistics, data-type casts, and whether `SELECT *` is unnecessarily fetching large columns. If the query returns a large number of rows, even an index won't make the result cheap.

The key production-debugging flow is:

```text
Slow query
    ↓
EXPLAIN ANALYZE
    ↓
Is it using an appropriate index?
    ↓
How many rows estimated vs actual?
    ↓
How many rows returned?
    ↓
Check I/O / buffers
    ↓
Check indexes + statistics
    ↓
Optimize query/index/schema
```

For a **Go + PostgreSQL backend interview**, a very common follow-up is: **"You added `(customer_id, status)` but PostgreSQL still does a sequential scan. Why?"** That's where selectivity, table size, statistics, visibility map, and cost estimates become important.
