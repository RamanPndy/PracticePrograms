class DisjointSet:
    '''
    A class to represent a disjoint set (union-find) data structure.
    Supports union and find operations with path compression and union by rank.
    TC: O(α(n)) for find and union operations (α is the inverse Ackermann function)
    SC: O(n) for storing parent and rank arrays
    '''
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False  # Already connected

        # Union by rank
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

def kruskal(nodes, edges):
    """
    nodes: number of nodes (assumed labeled 0 to n-1)
    edges: list of tuples (weight, node1, node2)
    Returns the edges in the Minimum Spanning Tree (MST) using Kruskal's algorithm.
    TC: O(E log E) where E is the number of edges (for sorting)
    SC: O(V) for storing the disjoint set
    """
    ds = DisjointSet(nodes)
    mst = []

    # Sort edges by weight
    edges.sort(key=lambda x: x[0])

    for weight, u, v in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))

    return mst

nodes = 4
edges = [
    (2, 0, 1),
    (3, 0, 2),
    (1, 1, 2),
    (4, 1, 3),
    (5, 2, 3)
]

mst = kruskal(nodes, edges)
print("Edges in MST:")
for u, v, w in mst:
    print(f"{u} -- {v} == {w}")

# Output:
# Edges in MST:
# 1 -- 2 == 1
# 0 -- 1 == 2
# 0 -- 2 == 3
# 1 -- 3 == 4
# 2 -- 3 == 5