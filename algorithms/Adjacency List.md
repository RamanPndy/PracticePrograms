
What is an Adjacency List?

A graph adjacency list stores for each vertex a list of all vertices directly connected to it.
It is the most common representation for sparse graphs.

Suppose the graph has edges:
1 → 2
1 → 3
2 → 4
3 → 4
4 → 1

Adjacency List Representation
1: [2, 3]
2: [4]
3: [4]
4: [1]

Directed Graph
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def print_graph(self):
        for node in self.adj:
            print(f"{node}: {self.adj[node]}")

Undirected Graph (bidirectional)
def add_edge(self, u, v):
    self.adj[u].append(v)
    self.adj[v].append(u)


Weighted Graph
class WeightedGraph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.adj[u].append((v, weight))

Advantages of Adjacency List
| Feature          | Explanation                   |
| ---------------- | ----------------------------- |
| Memory efficient | Stores only existing edges    |
| Fast traversal   | Iterate neighbors in O(E)     |
| Scales well      | Ideal for large sparse graphs |

Graph (Adjacency List) + BFS + DFS
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v, undirected=False):
        self.adj[u].append(v)
        if undirected:
            self.adj[v].append(u)

    # ----- BFS -----
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        order = []

        visited.add(start)

        while queue:
            node = queue.popleft()
            order.append(node)

            for neigh in self.adj[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append(neigh)

        return order

    # ----- DFS Recursive -----
    def dfs_recursive(self, start):
        visited = set()
        order = []

        def dfs(node):
            visited.add(node)
            order.append(node)

            for neigh in self.adj[node]:
                if neigh not in visited:
                    dfs(neigh)

        dfs(start)
        return order

    # ----- DFS Iterative -----
    def dfs_iterative(self, start):
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)

                # Push neighbors in reverse for natural order
                for neigh in reversed(self.adj[node]):
                    if neigh not in visited:
                        stack.append(neigh)

        return order

Explanation
BFS (Breadth-First Search)
1.Uses queue
2.Traverses level by level
3.Useful for shortest path in unweighted graph

DFS (Depth-First Search)
1.Uses stack (implicit via recursion or explicit)
2.Goes deep before wide

Useful for:
- Cycle detection
- Topological sort
- Connected components