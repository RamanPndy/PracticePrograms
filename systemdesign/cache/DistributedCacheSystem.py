'''
Components
 - Cache Nodes: 
    These are the servers where cached data is stored. Each cache node is responsible for storing a subset of the total cache.
 - Clients: Applications or services that interact with the cache system to read or write data.
 - Coordinator (optional): A service that helps in managing the cache nodes, data partitioning, and consistency.
 - Data Partitioner: A mechanism to determine how data is distributed across cache nodes (e.g., consistent hashing).
 - Replication Manager: Ensures data redundancy for fault tolerance.
 - Cache Manager: Manages the lifecycle of cached data, including expiration and eviction policies.

 Design Considerations
 - Data Partitioning: Use consistent hashing to distribute keys across cache nodes to ensure balanced load.
 - Replication: Store copies of data on multiple nodes to ensure high availability and fault tolerance.
 - Consistency: Implement mechanisms to ensure data consistency across replicas (e.g., using quorum reads/writes).
 - Eviction Policy: Decide on an eviction policy (e.g., LRU, LFU) to manage limited cache space.
 - Expiration: Implement time-to-live (TTL) for cache entries to ensure stale data is not served.
 - Scalability: Ensure the system can scale horizontally by adding more cache nodes.
 - Fault Tolerance: Detect node failures and redistribute data as needed.

 Detailed Components
1. Cache Nodes
Storage: In-memory storage (e.g., Redis, Memcached) for fast access.
Communication: Nodes communicate using a protocol like gRPC or HTTP.
Monitoring: Each node monitors its health and reports to the coordinator.
2. Clients
Cache Client Library: Provides methods to get, put, and delete data in the cache.
Consistent Hashing: The client library uses consistent hashing to determine which node to interact with for a given key.
3. Coordinator
Node Management: Keeps track of active cache nodes and their status.
Partition Management: Manages consistent hashing ring and handles node additions/removals.
Failure Detection: Monitors nodes and triggers data redistribution on failures.
4. Data Partitioner
Consistent Hashing: Ensures that each key is mapped to a specific cache node.
Virtual Nodes: Improves load balancing by mapping keys to virtual nodes, which are then mapped to physical nodes.
5. Replication Manager
Replication Factor: Defines the number of replicas for each data entry.
Consistency Protocol: Ensures data consistency across replicas (e.g., using Paxos or Raft).
6. Cache Manager
Eviction Policies: Implements LRU, LFU, or other eviction policies.
TTL Management: Manages expiration of cache entries based on TTL.
Data Flow
Write Operation:

Client calculates the hash of the key and determines the target cache node using consistent hashing.
Client sends the write request to the primary node and replication nodes.
Replication manager ensures that the data is replicated to the required number of nodes.
Write success is acknowledged once the data is written to the required quorum of nodes.
Read Operation:

Client calculates the hash of the key and determines the target cache node using consistent hashing.
Client sends a read request to the primary node.
If the primary node fails, the client retries the read request on one of the replication nodes.
Data is returned to the client if found; otherwise, it returns a cache miss.
Fault Tolerance and Recovery
Heartbeat Mechanism: Cache nodes send regular heartbeat messages to the coordinator.
Failure Detection: The coordinator marks a node as failed if heartbeats are missed.
Data Redistribution: Upon node failure, the coordinator redistributes data to other nodes to maintain replication factor.
'''
class CacheNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.storage = {}
        self.health = True  # Node health status

    def get(self, key):
        return self.storage.get(key)

    def put(self, key, value):
        self.storage[key] = value

    def delete(self, key):
        if key in self.storage:
            del self.storage[key]

class ConsistentHashing:
    def __init__(self, nodes):
        self.nodes = nodes
        self.ring = self.create_ring(nodes)

    def create_ring(self, nodes):
        ring = {}
        for node in nodes:
            hash_key = hash(node.node_id)
            ring[hash_key] = node
        return ring

    def get_node(self, key):
        hash_key = hash(key)
        node_hash = min(self.ring.keys(), key=lambda x: abs(x - hash_key))
        return self.ring[node_hash]

class CacheClient:
    def __init__(self, partitioner):
        self.partitioner = partitioner

    def get(self, key):
        node = self.partitioner.get_node(key)
        return node.get(key)

    def put(self, key, value):
        node = self.partitioner.get_node(key)
        node.put(key, value)

# Example usage
nodes = [CacheNode(i) for i in range(5)]
partitioner = ConsistentHashing(nodes)
client = CacheClient(partitioner)

# Put and get values
client.put("key1", "value1")
print(client.get("key1"))  # Output: value1
