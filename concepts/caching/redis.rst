how redis concurrency works ?
Redis, an in-memory data structure store, handles concurrency using a combination of its single-threaded event loop and 
various mechanisms to ensure atomicity and data consistency.
Redis's concurrency model is largely based on its single-threaded design, which simplifies the handling of concurrent 
operations and ensures data consistency. 
By leveraging atomic commands, transactions, pipelining, Lua scripting, and Pub/Sub mechanisms, Redis efficiently manages 
concurrency and provides robust data operations.
Redis manages concurrent writes using its single-threaded event loop, ensuring that all operations are processed sequentially. 
This design eliminates the need for complex locking mechanisms and guarantees that each command is executed atomically.

Single-threaded Event Loop
Redis operates on a single-threaded event loop, meaning it processes one command at a time in a first-come, first-served manner.
This means that when multiple clients send write commands to Redis simultaneously, the server will handle these commands sequentially.
Each write operation will be fully completed before the next one begins. 
This design ensures that data integrity is maintained without the risk of race conditions.
This design choice simplifies the handling of concurrent operations by eliminating the need for locks, 
which can be complex and error-prone in a multi-threaded environment. 
Because Redis processes commands sequentially, it inherently avoids race conditions.

Atomic Operations
Many of Redis's commands are atomic, meaning they will complete fully before another command is executed.
This includes commands like SET, INCR, DECR, LPUSH, and others.
tomic commands ensure that the entire operation is performed as a single, indivisible step, preventing other operations from interleaving. 
For example, when an INCR command is executed, Redis guarantees that the increment operation will complete without 
interference from other commands.
For instance, commands like INCR, DECR, and LPUSH ensure that operations are performed as a single, indivisible step. 
This guarantees that no other command can interfere with the operation while it is being executed, 
providing a consistent view of the data.

Transactions
Redis supports transactions through the use of the MULTI, EXEC, DISCARD, and WATCH commands. 
Transactions allow multiple commands to be queued up and executed atomically. 
The WATCH command can be used to implement optimistic locking, ensuring that the transaction only executes 
if the watched keys remain unchanged.

Here's a brief overview of how transactions work:
MULTI: Start a transaction block.
Commands: Queue up commands.
EXEC: Execute all queued commands atomically.
DISCARD: Discard all queued commands.

Example:
MULTI
SET key1 value1
SET key2 value2
EXEC

Optimistic Locking with WATCH
Redis provides optimistic locking using the WATCH command. 
This allows clients to watch one or more keys and ensure that they haven't been modified before executing a transaction. 
If any watched key is modified by another client, the transaction will be aborted.

Example using WATCH:
WATCH key1
MULTI
SET key1 newValue
EXEC

If key1 is modified by another client between the WATCH and EXEC commands, the transaction will fail.

Pipelining
Redis supports command pipelining, which allows a client to send multiple commands to the server without waiting for the 
responses of previous commands. 
This reduces the latency caused by round-trip times between client and server. 
However, pipelining doesn't change the fact that commands are still executed sequentially by the server.

LUA Scripting
Redis allows for the execution of Lua scripts using the EVAL command. 
Lua scripts are executed atomically, ensuring that all operations within the script are completed without interruption. 
This feature can be used to perform complex operations that would otherwise require multiple commands, ensuring atomicity and consistency.
Lua scripts in Redis are executed atomically, similar to transactions.
This means that all operations within a Lua script are completed without interruption. 

Example of a Lua script:
redis.call("SET", "key1", "value1")
redis.call("SET", "key2", "value2")
return redis.call("GET", "key1")

Pub/Sub
For real-time messaging, Redis provides a Publish/Subscribe (Pub/Sub) mechanism. 
While Pub/Sub doesn't provide guaranteed delivery or persistence, it allows for the efficient broadcasting of messages to 
multiple subscribers. 
Each message is processed in the order it was received, maintaining the single-threaded model.