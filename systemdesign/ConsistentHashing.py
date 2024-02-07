import hashlib

class ConsistentHashing:
    '''
    Consistent hashing is a technique used in distributed systems for partitioning data 
    across multiple nodes while minimizing the impact of node additions or removals.

    ConsistentHashing class represents a consistent hashing ring with support for 
    adding and removing nodes, as well as getting the node responsible for a given key.
    add_node method adds a node to the hashing ring by adding multiple virtual nodes (replicas) to the ring.
    remove_node method removes a node from the hashing ring by removing its virtual nodes.
    get_node method returns the node responsible for a given key by traversing the 
    hashing ring and finding the next node after the hashed key.
    _hash method hashes the input key using MD5 and returns an integer value.
    '''
    def __init__(self, nodes=None, replicas=3):
        self.replicas = replicas
        self.hash_ring = {}
        self.sorted_keys = []

        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node):
        for i in range(self.replicas):
            virtual_node = f"{node}-replica-{i}"
            hash_key = self._hash(virtual_node)
            self.hash_ring[hash_key] = node
            self.sorted_keys.append(hash_key)
        self.sorted_keys.sort()

    def remove_node(self, node):
        for i in range(self.replicas):
            virtual_node = f"{node}-replica-{i}"
            hash_key = self._hash(virtual_node)
            del self.hash_ring[hash_key]
            self.sorted_keys.remove(hash_key)

    def get_node(self, key):
        if not self.hash_ring:
            return None

        hash_key = self._hash(key)
        for ring_key in self.sorted_keys:
            if hash_key <= ring_key:
                return self.hash_ring[ring_key]
        return self.hash_ring[self.sorted_keys[0]]

    def _hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

# Example usage
if __name__ == "__main__":
    nodes = ["node1", "node2", "node3"]
    consistent_hashing = ConsistentHashing(nodes=nodes)

    # Add a new node
    consistent_hashing.add_node("node4")

    # Get node for a key
    print("Node for 'key1':", consistent_hashing.get_node("key1"))

    # Remove a node
    consistent_hashing.remove_node("node2")

    # Get node for a key after removing a node
    print("Node for 'key2':", consistent_hashing.get_node("key2"))
