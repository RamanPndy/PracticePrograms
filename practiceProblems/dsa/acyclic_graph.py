class DAG:
    '''
    A class to represent a Directed Acyclic Graph (DAG).
    Supports adding vertices and edges, and checks for cycles when adding edges.
    TC: O(V + E) for adding an edge (V = vertices, E = edges)
    SC: O(V + E) for storing the graph in an adjacency list
    '''
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        # Add vertices if not already present
        self.add_vertex(u)
        self.add_vertex(v)

        # Check if adding the edge creates a cycle
        if self._has_path(v, u):  # cycle check: v → u exists means adding u → v would create a cycle
            raise ValueError(f"Adding edge {u} -> {v} would create a cycle!")

        self.graph[u].append(v)

    def _has_path(self, src, dest, visited=None):
        if visited is None:
            visited = set()
        if src == dest:
            return True
        visited.add(src)
        for neighbor in self.graph.get(src, []):
            if neighbor not in visited:
                if self._has_path(neighbor, dest, visited):
                    return True
        return False

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

dag = DAG()
dag.add_edge("A", "B")
dag.add_edge("A", "C")
dag.add_edge("B", "D")
dag.add_edge("C", "D")
dag.display()
