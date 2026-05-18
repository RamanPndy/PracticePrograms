Topological Sort – DFS Method
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)  # u → v

    # Topological Sort using DFS
    def topo_sort_dfs(self):
        visited = set()
        stack = []

        def dfs(node):
            visited.add(node)
            for neigh in self.adj[node]:
                if neigh not in visited:
                    dfs(neigh)
            stack.append(node)

        # DFS from all nodes (handles disconnected graph)
        for node in self.adj:
            if node not in visited:
                dfs(node)

        return stack[::-1]  # reverse to get topo order


Kahn’s Algorithm (BFS + Indegree)
Kahn’s Algorithm is a method to perform Topological Sorting on a Directed Acyclic Graph (DAG) using BFS + Indegree calculation
Topological sort orders nodes such that:
For every edge U → V, U appears before V in the ordering.
This is used in:
- Task scheduling
- Build systems (make)
- Course prerequisite planning
- Dependency resolution

Indegree(node) = How many edges are coming into the node.
A → B → C
Indegree:
A: 0
B: 1
C: 1
A node with indegree 0 means it has no prerequisites → can be processed now.

Kahn’s Algorithm Steps (Simple!)
1. Compute indegree of all nodes.
2. Put all nodes with indegree = 0 into a queue.
3. While queue is not empty:
    - Remove a node from queue → add to answer
    - For each of its neighbors:
        - Reduce their indegree by 1
        - If some neighbor’s indegree becomes 0 → push to queue
4. If all nodes are processed → we have a valid topological order
Else → the graph has a cycle (not a DAG)

Example:
Graph
5 → 0  
5 → 2  
4 → 0  
4 → 1  
2 → 3  
3 → 1

Indegrees
0: 2 (from 5,4)
1: 2 (from 4,3)
2: 1 (from 5)
3: 1 (from 2)
4: 0
5: 0

What is Kahn’s Algorithm?

| Term              | Meaning                                 |
| ----------------- | --------------------------------------- |
| **Indegree**      | How many edges come into a node         |
| **Queue**         | BFS-like processing of 0-indegree nodes |
| **Goal**          | Build a valid topological order         |
| **Detect Cycle?** | YES — if nodes remain with indegree > 0 |


from collections import defaultdict, deque

class Graph2:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)

    # Kahn's Algorithm
    def topo_sort_kahn(self):
        indegree = defaultdict(int)

        # Compute indegree for each node
        for u in self.adj:
            for v in self.adj[u]:
                indegree[v] += 1
            if u not in indegree:
                indegree[u] = 0

        # Queue of all zero-indegree nodes
        queue = deque([node for node in indegree if indegree[node] == 0])
        topo = []

        while queue:
            node = queue.popleft()
            topo.append(node)

            for neigh in self.adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)

        # If not all nodes were processed → cycle
        if len(topo) != len(indegree):
            raise ValueError("Graph has a cycle! Not a DAG.")

        return topo

Which One Should You Use?
| Method                   | When to Use                          | Pros                                      |
| ------------------------ | ------------------------------------ | ----------------------------------------- |
| **DFS Topological Sort** | Simple, recursive                    | Easy implementation, no indegree tracking |
| **Kahn’s Algorithm**     | You need cycle detection + BFS order | Detects cycles automatically, iterative   |
