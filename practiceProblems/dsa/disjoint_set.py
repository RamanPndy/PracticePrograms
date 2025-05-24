class DisjointSet:
    '''
    A Disjoint Set (Union-Find) data structure with path compression and union by rank.
    Supports union and find operations.
    TC: O(α(n)) for find and union operations, where α is the inverse Ackermann function.
    SC: O(n) for storing parent and rank arrays
    '''
    def __init__(self, n):
        # parent[i] points to parent of i; if parent[i] == i, i is root
        self.parent = list(range(n))
        self.rank = [0] * n  # Used for union by rank

    def find(self, x):
        if self.parent[x] != x:
            # Path compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

ds = DisjointSet(5)

ds.union(0, 1)
ds.union(1, 2)
print(ds.connected(0, 2))  # True

print(ds.connected(0, 3))  # False

ds.union(3, 4)
print(ds.connected(3, 4))  # True

ds.union(2, 4)
print(ds.connected(0, 4))  # True
