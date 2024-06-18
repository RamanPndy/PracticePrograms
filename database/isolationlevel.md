Database isolation levels determine the visibility of changes made by one transaction to other concurrent transactions. They balance between data consistency and system performance. The ANSI SQL standard defines four isolation levels:

1. **Read Uncommitted**
2. **Read Committed**
3. **Repeatable Read**
4. **Serializable**

### Read Uncommitted

**Definition**: Allows transactions to read data that has been modified but not yet committed by other transactions. This can lead to dirty reads, non-repeatable reads, and phantom reads.

**Example**:
- **Transaction 1**: Starts and updates a row but hasn't committed.
- **Transaction 2**: Reads the updated row, seeing uncommitted changes.

```sql
-- Transaction 1
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 'A';

-- Transaction 2
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT balance FROM accounts WHERE account_id = 'A'; -- Sees the uncommitted balance
```

### Read Committed

**Definition**: Prevents dirty reads by ensuring that a transaction can only read committed data. However, non-repeatable reads and phantom reads can still occur.

**Example**:
- **Transaction 1**: Starts, updates a row, and commits.
- **Transaction 2**: Reads the updated row only after the commit.

```sql
-- Transaction 1
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 'A';
COMMIT;

-- Transaction 2
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SELECT balance FROM accounts WHERE account_id = 'A'; -- Sees the committed balance
```

### Repeatable Read

**Definition**: Ensures that if a transaction reads a row, it will see the same data throughout its duration, preventing non-repeatable reads. However, phantom reads can still occur.

**Example**:
- **Transaction 1**: Starts and reads a row.
- **Transaction 2**: Updates and commits the row read by Transaction 1.
- **Transaction 1**: Reads the row again and sees the same data as before.

```sql
-- Transaction 1
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN;
SELECT balance FROM accounts WHERE account_id = 'A'; -- Sees the initial balance

-- Transaction 2
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 'A';
COMMIT;

-- Transaction 1
SELECT balance FROM accounts WHERE account_id = 'A'; -- Sees the initial balance (unchanged)
```

### Serializable

**Definition**: The highest isolation level, ensuring complete isolation from other transactions. It prevents dirty reads, non-repeatable reads, and phantom reads, effectively serializing transaction execution.

**Example**:
- **Transaction 1**: Starts and reads a row.
- **Transaction 2**: Tries to update the same row but is blocked until Transaction 1 completes.

```sql
-- Transaction 1
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;
SELECT balance FROM accounts WHERE account_id = 'A'; -- Sees the initial balance

-- Transaction 2
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 'A'; -- Blocked until Transaction 1 completes

-- Transaction 1
COMMIT; -- Now Transaction 2 can proceed
```

### Summary of Isolation Levels and Phenomena

| Isolation Level    | Dirty Reads | Non-repeatable Reads | Phantom Reads |
|--------------------|-------------|----------------------|---------------|
| Read Uncommitted   | Yes         | Yes                  | Yes           |
| Read Committed     | No          | Yes                  | Yes           |
| Repeatable Read    | No          | No                   | Yes           |
| Serializable       | No          | No                   | No            |

**Dirty Reads**: Transaction reads data written by another uncommitted transaction.
**Non-repeatable Reads**: Transaction reads the same row twice and gets different data each time.
**Phantom Reads**: Transaction reads a set of rows that satisfy a condition, but a subsequent read within the same transaction finds new rows that satisfy the same condition due to another committed transaction.

By understanding and using the appropriate isolation levels, you can balance the trade-offs between data consistency and system performance based on your application's requirements.