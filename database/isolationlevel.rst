what is DB isolation level ?
In the context of databases, isolation level refers to the level of data integrity and consistency maintained during transactions. 
Different isolation levels define how transactions interact with each other and how changes made by one transaction are visible to other concurrent transactions. 
The common isolation levels defined by the ANSI/ISO SQL standard are:

Read Uncommitted: 
This is the lowest isolation level where transactions can see uncommitted changes made by other transactions. 
It can lead to dirty reads, meaning a transaction can read data that has been modified but not yet committed by another transaction.

Read Committed: 
In this isolation level, a transaction can only see data that has been committed by other transactions. 
It prevents dirty reads but allows non-repeatable reads, where a transaction may see different values for the same record 
if it is updated by another transaction in between.

Repeatable Read: 
This level ensures that within a transaction, a query will always return the same set of rows. 
It prevents non-repeatable reads but allows phantom reads, where new rows can be inserted by other transactions between 
two reads of the same query.

Serializable: 
This is the highest isolation level that provides strict transaction isolation. 
It ensures that concurrent transactions do not affect each other, preventing dirty reads, non-repeatable reads, and 
phantom reads. However, it can also lead to a higher degree of locking and potentially affect performance.

Snapshot Isolation: 
Some databases offer a snapshot isolation level where each transaction sees a consistent snapshot of the database at the start
of the transaction. This can provide a higher level of concurrency compared to serializable isolation.

Choosing the right isolation level depends on the specific requirements of your application in terms of data consistency, 
concurrency, and performance.

Dirty Read:
when a transaction is allowed to read data from a row that has been modified by other running transaction and not yet committed.

Lost Update:
occurs when two processes reads the same data and then try to update the data with different value and one of the updates is lost.

Non Repeatable read:
occurs when, during the course of a transaction, a row is retrieved twice and the values within the row differ between reads.

Phantoms:
occurs when, in the course of a transaction, new rows are added or removed by another transaction to the records being read.

Serialization anamoly:
the result of successfully committing a group of transactions is inconsistent with all possible orderings of running those transactions one at a time.