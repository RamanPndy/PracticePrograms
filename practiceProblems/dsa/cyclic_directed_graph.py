class Graph:
    '''
    A class to represent a directed graph using adjacency list representation.
    Supports adding edges and checking for cycles using DFS.
    TC: O(V + E) for cycle detection (V = vertices, E = edges)
    SC: O(V) for visited and recursion stack arrays
    '''
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: [] for i in range(vertices)}  # adjacency list

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def _dfs_cycle_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True

        for neighbour in self.adj[v]:
            if not visited[neighbour]:
                if self._dfs_cycle_util(neighbour, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True  # cycle found

        rec_stack[v] = False
        return False

    def has_cycle(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V

        for node in range(self.V):
            if not visited[node]:
                if self._dfs_cycle_util(node, visited, rec_stack):
                    return True
        return False

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)  # creates a cycle
g.add_edge(2, 3)

print("Graph has cycle?" , g.has_cycle())  # Output: True

# If you remove the edge 2->0, cycle disappears:
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("Graph has cycle?" , g.has_cycle())  # Output: False
