A **PostgreSQL advisory lock** is a mechanism that allows you to implement application-level locking. Unlike traditional table-level or row-level locks, advisory locks are not tied to database transactions or tables and must be explicitly managed by the application. These locks are particularly useful for coordinating access to shared resources outside the database or implementing custom concurrency controls within the application.

### Key Features of Advisory Locks
1. **Application-Defined Context**:
   - The locks are identified using user-defined integers or pairs of integers (`bigint`).
   - The application assigns meaning to these numbers (e.g., resource IDs or custom categories).

2. **Session-Based or Transaction-Based**:
   - Advisory locks can either persist for the duration of a session or be automatically released at the end of a transaction.

3. **Lightweight**:
   - They are implemented in shared memory, making them faster and less resource-intensive compared to traditional locks.

4. **Exclusive and Shared Modes**:
   - PostgreSQL supports both exclusive (`pg_try_advisory_lock`) and shared (`pg_try_advisory_lock_shared`) locks.

### Use Cases
- **Preventing Duplicate Processing**:
  To ensure that only one application instance processes a particular task.
- **Coordinating Access to External Resources**:
  Synchronizing access to files or external services.
- **Custom Resource Locks**:
  Locking on application-defined resources rather than database tables.

### Examples

#### Session-Based Exclusive Lock
```sql
-- Attempt to acquire an advisory lock
SELECT pg_advisory_lock(12345);

-- Do some critical work here

-- Release the lock
SELECT pg_advisory_unlock(12345);
```

#### Transaction-Based Lock
```sql
-- Acquire a lock within a transaction
BEGIN;
SELECT pg_advisory_xact_lock(12345);

-- Critical section
COMMIT; -- The lock is released automatically
```

#### Shared Lock
```sql
-- Shared locks allow multiple processes to hold the lock
SELECT pg_advisory_lock_shared(12345);
```

#### Non-Blocking Lock Attempt
```sql
-- Try acquiring the lock without blocking if it is already held
SELECT pg_try_advisory_lock(12345);
```

### Functions for Advisory Locks
1. **`pg_advisory_lock(key)`**:
   Acquires an exclusive advisory lock.
2. **`pg_advisory_lock_shared(key)`**:
   Acquires a shared advisory lock.
3. **`pg_try_advisory_lock(key)`**:
   Attempts to acquire an exclusive advisory lock without blocking.
4. **`pg_advisory_xact_lock(key)`**:
   Acquires an advisory lock that is released automatically at the end of the transaction.
5. **`pg_advisory_unlock(key)`**:
   Releases the specified advisory lock.

### Notes
- Advisory locks are not visible to other transactions unless explicitly checked.
- Improper use (e.g., failing to release locks) can cause resource contention or deadlocks.
- Use advisory locks carefully when multiple applications interact with the same PostgreSQL instance.

### Documentation
For more details, refer to the [PostgreSQL Advisory Lock documentation](https://www.postgresql.org/docs/current/functions-admin.html#FUNCTIONS-ADVISORY-LOCKS).