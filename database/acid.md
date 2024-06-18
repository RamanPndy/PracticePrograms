ACID is a set of properties that ensure reliable processing of database transactions. ACID stands for Atomicity, Consistency, Isolation, and Durability. Here’s an explanation of each property with examples:

### Atomicity
Atomicity ensures that all operations within a transaction are completed successfully. If any part of the transaction fails, the entire transaction is rolled back, leaving the database in its original state.

**Example**:
Imagine a banking application where you need to transfer $100 from Account A to Account B.

- **Step 1**: Debit $100 from Account A
- **Step 2**: Credit $100 to Account B

If the system crashes after Step 1 but before Step 2, the transaction would be rolled back, and both accounts would remain unchanged, ensuring that $100 is neither lost nor incorrectly recorded.

```sql
BEGIN TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE account_id = 'A';
UPDATE accounts SET balance = balance + 100 WHERE account_id = 'B';

COMMIT; -- If any operation fails, ROLLBACK
```

### Consistency
Consistency ensures that a transaction brings the database from one valid state to another, maintaining the database’s integrity constraints.

**Example**:
Consider a database constraint that the total balance of all accounts should always be $1000.

- Before the transaction: Total balance is $1000.
- Transfer $100 from Account A to Account B.

The consistency property ensures that after the transaction, the total balance remains $1000.

```sql
-- Initial state: Account A = $500, Account B = $500, Total = $1000

BEGIN TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE account_id = 'A';
UPDATE accounts SET balance = balance + 100 WHERE account_id = 'B';

-- Final state: Account A = $400, Account B = $600, Total = $1000

COMMIT;
```

### Isolation
Isolation ensures that concurrent transactions execute independently of each other. The intermediate state of a transaction is not visible to other transactions.

**Example**:
Suppose two transactions are occurring simultaneously:
- Transaction 1: Transfer $100 from Account A to Account B.
- Transaction 2: Transfer $50 from Account B to Account A.

Isolation ensures that each transaction sees the database in a consistent state and their operations do not interfere with each other.

Without isolation, one transaction might read intermediate results of another, leading to inconsistencies. Database systems use isolation levels (e.g., READ COMMITTED, SERIALIZABLE) to manage this.

```sql
-- Transaction 1
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 'A';
UPDATE accounts SET balance = balance + 100 WHERE account_id = 'B';
COMMIT;

-- Transaction 2
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 50 WHERE account_id = 'B';
UPDATE accounts SET balance = balance + 50 WHERE account_id = 'A';
COMMIT;
```

### Durability
Durability ensures that once a transaction is committed, it will remain so, even in the event of a system failure.

**Example**:
After successfully transferring $100 from Account A to Account B, the changes are saved permanently. If the system crashes immediately after the transaction commits, the new account balances are preserved.

```sql
BEGIN TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE account_id = 'A';
UPDATE accounts SET balance = balance + 100 WHERE account_id = 'B';

COMMIT; -- Changes are now permanent and will survive system crashes
```

### Summary with Example Transaction

Here’s a complete example demonstrating all ACID properties in the context of a money transfer:

```sql
-- Assume the initial state:
-- Account A = $1000
-- Account B = $500

-- Atomicity: Transaction will either fully complete or not at all
-- Consistency: Total balance before and after the transaction must be $1500
-- Isolation: Concurrent transactions do not interfere with each other
-- Durability: Changes persist even after a system crash

BEGIN TRANSACTION;

-- Step 1: Debit $100 from Account A
UPDATE accounts SET balance = balance - 100 WHERE account_id = 'A';

-- Step 2: Credit $100 to Account B
UPDATE accounts SET balance = balance + 100 WHERE account_id = 'B';

-- Commit the transaction
COMMIT;

-- After transaction:
-- Account A = $900
-- Account B = $600
-- Total = $1500
```

In this example, all ACID properties are ensured, providing a reliable and consistent transaction process.