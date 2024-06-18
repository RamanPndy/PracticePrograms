In MariaDB, a transaction is a sequence of one or more SQL statements that are executed as a single unit of work. Transactions ensure that either all operations within the transaction are completed successfully or none of them are applied, maintaining the integrity and consistency of the database. This is especially important in scenarios where multiple operations depend on each other.

### Key Properties of Transactions (ACID)
- **Atomicity**: Ensures that all operations within a transaction are completed successfully. If any part of the transaction fails, the entire transaction is rolled back.
- **Consistency**: Ensures that a transaction brings the database from one valid state to another, maintaining all defined rules and constraints.
- **Isolation**: Ensures that transactions operate independently, with intermediate states of a transaction not visible to other transactions.
- **Durability**: Ensures that once a transaction is committed, the changes are permanent, even in the event of a system failure.

### Transaction Commands in MariaDB

1. **BEGIN**: Starts a new transaction.
2. **COMMIT**: Ends the current transaction and makes all changes permanent.
3. **ROLLBACK**: Ends the current transaction and undoes all changes made within the transaction.
4. **SAVEPOINT**: Sets a savepoint within a transaction to which you can later roll back.
5. **ROLLBACK TO SAVEPOINT**: Rolls back to a specified savepoint within a transaction.

### Example Usage

#### Starting a Transaction
```sql
BEGIN;
```

#### Performing Operations
```sql
UPDATE accounts SET balance = balance - 100 WHERE account_id = 'A';
UPDATE accounts SET balance = balance + 100 WHERE account_id = 'B';
```

#### Committing the Transaction
```sql
COMMIT;
```

#### Rolling Back a Transaction
```sql
ROLLBACK;
```

#### Using Savepoints
```sql
BEGIN;

UPDATE accounts SET balance = balance - 100 WHERE account_id = 'A';
SAVEPOINT before_credit;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 'B';

-- Something goes wrong, rollback to savepoint
ROLLBACK TO SAVEPOINT before_credit;

-- Finalize transaction
COMMIT;
```

### Example Scenario: Money Transfer
Here's a full example demonstrating a money transfer between two accounts within a transaction:

```sql
BEGIN;

-- Deduct $100 from Account A
UPDATE accounts SET balance = balance - 100 WHERE account_id = 'A';

-- Add $100 to Account B
UPDATE accounts SET balance = balance + 100 WHERE account_id = 'B';

-- Commit the transaction
COMMIT;
```

### Handling Transactions in Programming Languages
When interacting with MariaDB from programming languages like Python, you typically use a database connector that provides transaction management methods. Here's an example using Python's `mysql-connector`:

```python
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password',
    database='dbname'
)

try:
    cursor = conn.cursor()
    conn.start_transaction()

    cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE account_id = 'A'")
    cursor.execute("UPDATE accounts SET balance = balance + 100 WHERE account_id = 'B'")

    conn.commit()
except mysql.connector.Error as err:
    conn.rollback()
    print(f"Error: {err}")
finally:
    cursor.close()
    conn.close()
```

### Conclusion
Transactions in MariaDB are essential for ensuring data integrity and consistency, especially in multi-step operations that need to be executed as a single unit of work. By using transaction control commands like `BEGIN`, `COMMIT`, and `ROLLBACK`, you can manage complex operations effectively and handle potential errors gracefully.