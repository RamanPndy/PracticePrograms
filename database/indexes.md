If you're preparing for a **PostgreSQL/backend interview**, it's useful to think about indexes in two dimensions:

1. **Index structure** — B-tree, Hash, GIN, GiST, BRIN, etc.
2. **How the index is defined** — single-column, composite, partial, expression, covering (`INCLUDE`).

The key idea is:

> An index is an additional data structure that lets PostgreSQL find qualifying rows without scanning the entire table.

---

# 1. B-tree — default and most important

```sql
CREATE INDEX idx_orders_customer
ON orders(customer_id);
```

PostgreSQL's default index type is **B-tree**.

Conceptually:

```text
                 50
              /      \
           20          80
         /   \        /   \
       10    30     60    90
```

The tree remains balanced, so searching is approximately:

```text
O(log N)
```

### Good for

Equality:

```sql
WHERE customer_id = 123
```

Ranges:

```sql
WHERE amount > 1000
```

```sql
WHERE created_at BETWEEN '2026-01-01' AND '2026-02-01'
```

Sorting:

```sql
ORDER BY created_at
```

Prefix matching:

```sql
WHERE name LIKE 'Ram%'
```

### Not good for

```sql
WHERE name LIKE '%ram%'
```

because the wildcard is at the beginning.

### Use B-tree for

Most normal application queries.

If you're unsure which index to use, **B-tree is usually the first one to investigate**.

---

# 2. Composite / multicolumn B-tree

Example:

```sql
CREATE INDEX idx_orders_customer_status
ON orders(customer_id, status);
```

This is especially relevant to your previous query:

```sql
SELECT *
FROM orders
WHERE customer_id = 123
  AND status = 'active';
```

Think of the index as sorted by:

```text
customer_id
    ↓
status
    ↓
rows
```

For example:

```text
customer_id  status
-----------  ------
100          active
100          cancelled
101          active
101          pending
123          active
123          active
123          cancelled
124          active
```

PostgreSQL can jump directly to:

```text
customer_id = 123
```

and then find:

```text
status = active
```

### Column order matters

Compare:

```sql
(customer_id, status)
```

vs:

```sql
(status, customer_id)
```

With:

```sql
WHERE customer_id = 123
```

the first index is much more useful.

With:

```sql
WHERE status = 'active'
```

the second may be more useful.

A useful mental model is the **leftmost prefix**:

```text
INDEX(a, b, c)

Useful for:

a
a + b
a + b + c

Potentially less useful for:

b
c
b + c
```

There are nuances in modern PostgreSQL's planner, so don't treat this as an absolute rule, but it's an excellent starting point.

---

# 3. Hash index

```sql
CREATE INDEX idx_customer_hash
ON customers USING HASH(customer_id);
```

Conceptually:

```text
hash(customer_id)
       ↓
    bucket
       ↓
     row
```

It's designed primarily for **equality**:

```sql
WHERE customer_id = 123
```

### Good for

```sql
=
```

### Not useful for

```sql
>
<
BETWEEN
ORDER BY
```

For example:

```sql
WHERE customer_id > 100
```

A B-tree is much better suited.

### Practical point

In PostgreSQL, **B-tree is usually preferred even for equality queries**, because it also supports ranges and ordering.

So Hash indexes have relatively specialized use cases.

---

# 4. GIN — great for JSON, arrays, full-text search

GIN = **Generalized Inverted Index**.

Imagine you have:

```sql
products
---------
id
name
tags
```

where:

```text
tags = ['electronics', 'mobile', 'android']
```

A GIN index can create an inverted structure roughly like:

```text
electronics → product 1, product 7, product 21
mobile      → product 1, product 4
android     → product 1, product 9
```

Create:

```sql
CREATE INDEX idx_products_tags
ON products USING GIN(tags);
```

Then:

```sql
SELECT *
FROM products
WHERE tags @> ARRAY['android'];
```

can benefit from the GIN index.

---

## GIN + JSONB

Extremely common in PostgreSQL.

```sql
CREATE INDEX idx_orders_metadata
ON orders USING GIN(metadata);
```

For:

```json
{
  "payment": "upi",
  "city": "Bangalore",
  "source": "mobile"
}
```

Queries involving JSONB containment/existence can use GIN.

Example:

```sql
SELECT *
FROM orders
WHERE metadata @> '{"payment": "upi"}';
```

### Good for

* JSONB
* Arrays
* Full-text search
* Membership/containment queries

### Tradeoff

GIN indexes can be:

* large
* expensive to maintain
* slower to update than a simple B-tree

So don't put GIN on everything.

---

# 5. GiST

GiST = **Generalized Search Tree**.

It's a flexible index framework particularly useful for **spatial/range-like data** and certain specialized data types.

For example, PostgreSQL range types:

```sql
CREATE INDEX idx_booking_period
ON bookings USING GIST(booking_period);
```

Suppose:

```text
booking_period
--------------
10:00 - 12:00
13:00 - 15:00
```

You can query overlapping ranges:

```sql
WHERE booking_period &&
      '[11:00,14:00]'
```

GiST is also heavily used with **PostGIS** for spatial queries.

For example:

```text
Find restaurants within X km
Find geometries intersecting another geometry
Find overlapping shapes
```

### Good for

* Geospatial data
* Range queries
* Geometric relationships
* Certain specialized operators

---

# 6. SP-GiST

SP-GiST = **Space-Partitioned GiST**.

It's useful for data that naturally partitions into regions.

Examples include structures resembling:

```text
quadtrees
kd-trees
tries
```

It is more specialized than GiST.

You generally won't choose SP-GiST for ordinary:

```sql
customer_id
email
created_at
```

queries.

---

# 7. BRIN

BRIN = **Block Range Index**.

This is particularly interesting for **huge tables**.

Imagine a table containing:

```text
1 billion rows
```

and:

```text
created_at
```

was inserted approximately in chronological order:

```text
Block 1 → Jan 1
Block 2 → Jan 2
Block 3 → Jan 3
...
Block 100000 → Dec 31
```

BRIN doesn't store every row.

It stores summaries for blocks:

```text
Block       min date       max date
-------------------------------------
1           Jan 1          Jan 1
2           Jan 2          Jan 2
3           Jan 3          Jan 3
...
```

Query:

```sql
WHERE created_at >= '2026-09-01'
```

BRIN can eliminate huge numbers of blocks.

### Huge advantage

Very small index.

```text
B-tree → potentially large
BRIN   → tiny
```

### Good for

Very large tables where the indexed column has a strong correlation with physical row order.

Typical examples:

```text
created_at
timestamp
auto-increment ID
event sequence
```

### Bad scenario

If the values are completely random:

```text
Block 1 → values 1, 500000, 27, 900000...
Block 2 → values 42, 8000, 100...
```

BRIN can't eliminate many blocks effectively.

---

# 8. Unique index

```sql
CREATE UNIQUE INDEX idx_users_email
ON users(email);
```

This does two things:

1. Makes lookup efficient.
2. Enforces uniqueness.

So:

```sql
INSERT INTO users(email)
VALUES ('ram@example.com');
```

and another:

```sql
INSERT INTO users(email)
VALUES ('ram@example.com');
```

will violate the unique constraint.

Usually you'd define:

```sql
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    email TEXT UNIQUE
);
```

rather than manually creating the index.

---

# 9. Partial index

This is extremely useful in production.

Suppose:

```text
orders = 100 million rows
```

but only:

```text
5 million = active
95 million = completed/cancelled
```

Your application frequently asks:

```sql
WHERE customer_id = 123
AND status = 'active'
```

Instead of indexing all rows:

```sql
CREATE INDEX idx_orders_customer_status
ON orders(customer_id, status);
```

you could potentially create:

```sql
CREATE INDEX idx_active_orders_customer
ON orders(customer_id)
WHERE status = 'active';
```

Now the index contains **only active orders**.

That's potentially much smaller.

Query:

```sql
SELECT *
FROM orders
WHERE customer_id = 123
AND status = 'active';
```

can use it.

### Great for

* Active records
* Unprocessed jobs
* Non-deleted records
* Pending payments
* Current subscriptions

Example:

```sql
CREATE INDEX idx_pending_jobs
ON jobs(priority, created_at)
WHERE status = 'pending';
```

Very useful for job queues.

---

# 10. Expression index

Suppose you frequently do:

```sql
SELECT *
FROM users
WHERE LOWER(email) = 'ram@example.com';
```

A normal index:

```sql
CREATE INDEX idx_users_email
ON users(email);
```

may not efficiently support that expression.

Instead:

```sql
CREATE INDEX idx_users_lower_email
ON users(LOWER(email));
```

Now:

```sql
WHERE LOWER(email) = 'ram@example.com'
```

can use the index.

Other examples:

```sql
CREATE INDEX idx_users_year
ON users(EXTRACT(YEAR FROM created_at));
```

or functions/operators appropriate to the data type.

---

# 11. Covering index / INCLUDE

Suppose:

```sql
SELECT customer_id, amount
FROM orders
WHERE customer_id = 123;
```

You could have:

```sql
CREATE INDEX idx_orders_customer
ON orders(customer_id)
INCLUDE(amount);
```

The index contains:

```text
customer_id
amount
```

but `amount` is not part of the index's search ordering.

This can enable an **index-only scan** when PostgreSQL can satisfy the visibility requirements.

Useful when:

```text
WHERE columns
       +
SELECT columns
```

are known and frequently queried.

---

# 12. Index-only scan

This is an important interview concept.

Normally:

```text
Index
 ↓
Find row location
 ↓
Go to table
 ↓
Read row
```

With a covering index:

```text
Index
 ↓
Everything needed
 ↓
Return result
```

Potentially avoiding heap/table reads.

Example:

```sql
CREATE INDEX idx_orders_customer
ON orders(customer_id)
INCLUDE(amount, status);
```

Query:

```sql
SELECT amount, status
FROM orders
WHERE customer_id = 123;
```

may be able to use an index-only scan.

---

# 13. Full-text search indexes

For PostgreSQL full-text search, GIN is commonly used.

Example:

```sql
CREATE INDEX idx_articles_search
ON articles
USING GIN(to_tsvector('english', content));
```

Then:

```sql
WHERE to_tsvector('english', content)
      @@ plainto_tsquery('english', 'kubernetes kafka');
```

This is very different from:

```sql
LIKE '%kubernetes%'
```

For serious text search, PostgreSQL's full-text search or a dedicated search engine may be more appropriate.

---

# Practical decision table

| Requirement                    | Usually consider                           |
| ------------------------------ | ------------------------------------------ |
| `id = 123`                     | **B-tree**                                 |
| `amount > 1000`                | **B-tree**                                 |
| `created_at BETWEEN ...`       | **B-tree**                                 |
| `ORDER BY created_at`          | **B-tree**                                 |
| `customer_id + status`         | **Composite B-tree**                       |
| Unique email                   | **Unique B-tree**                          |
| `LIKE 'abc%'`                  | **B-tree**                                 |
| `LIKE '%abc%'`                 | Usually not normal B-tree                  |
| JSONB containment              | **GIN**                                    |
| Array containment              | **GIN**                                    |
| Full-text search               | **GIN**                                    |
| Geographic/spatial             | **GiST / SP-GiST**                         |
| Range overlap                  | **GiST**                                   |
| Massive time-series table      | **BRIN**                                   |
| Only active rows               | **Partial index**                          |
| `LOWER(email)`                 | **Expression index**                       |
| WHERE + SELECT columns         | **INCLUDE / covering index**               |
| Pure equality specialized case | Hash possible, but B-tree often sufficient |

---

# The most important interview concept: don't blindly add indexes

Suppose you have:

```sql
orders(
    id,
    customer_id,
    status,
    created_at,
    amount
)
```

And queries:

```sql
Q1:
WHERE customer_id = ?

Q2:
WHERE customer_id = ? AND status = ?

Q3:
WHERE customer_id = ?
ORDER BY created_at DESC
```

You shouldn't automatically create:

```text
index(customer_id)
index(status)
index(customer_id,status)
index(created_at)
index(customer_id,created_at)
```

That creates unnecessary indexes.

Every index has a cost:

```text
INSERT
  ↓
Update table
  +
Update every relevant index
```

So more indexes mean:

* More disk space
* More write overhead
* More WAL
* More vacuum/maintenance work
* Potentially slower INSERT/UPDATE/DELETE

The goal is:

> **Design indexes around actual query patterns, not individual columns.**

---

# A useful production example

Suppose you're building an order service.

Queries:

```sql
-- Get customer's active orders
SELECT id, amount
FROM orders
WHERE customer_id = ?
AND status = 'active'
ORDER BY created_at DESC
LIMIT 20;
```

I'd investigate an index like:

```sql
CREATE INDEX idx_orders_customer_status_created
ON orders(customer_id, status, created_at DESC)
INCLUDE(amount);
```

Now the index aligns with:

```text
WHERE
 ↓
customer_id
status
 ↓
ORDER BY
 ↓
created_at
 ↓
SELECT
 ↓
amount
```

Conceptually:

```text
(customer_id, status, created_at)
                         +
                       amount
                      (INCLUDE)
```

This is the kind of **query-driven index design** interviewers usually want to hear.

And I'd still verify it with:

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT ...
```

rather than assuming the index is beneficial.
