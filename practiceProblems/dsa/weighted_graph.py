class WeightedGraph:
    '''
    A class to represent a weighted undirected graph using an adjacency list.
    Supports adding nodes and edges with weights, and displaying the graph.
    TC: O(1) for adding a node, O(1) for adding an edge
    SC: O(V + E) for storing the graph in an adjacency list (V = vertices, E = edges)
    '''
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, u, v, weight):
        # Add nodes if they don't exist
        if u not in self.graph:
            self.add_node(u)
        if v not in self.graph:
            self.add_node(v)

        # For undirected graph, add edge both ways
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def get_neighbors(self, node):
        return self.graph.get(node, [])

    def display(self):
        for node in self.graph:
            print(f"{node}: ", end="")
            print(", ".join([f"({nbr}, weight={w})" for nbr, w in self.graph[node]]))

wg = WeightedGraph()
wg.add_edge('A', 'B', 5)
wg.add_edge('A', 'C', 3)
wg.add_edge('B', 'C', 2)
wg.add_edge('B', 'D', 4)

wg.display()
# Output:
# A: (B, weight=5), (C, weight=3)
# B: (A, weight=5), (C, weight=2), (D, weight=4)
# C: (A, weight=3), (B, weight=2)
# D: (B, weight=4)
# This code defines a WeightedGraph class that allows adding nodes and edges with weights,
# and displays the graph in a readable format. The graph is undirected, meaning edges are bidirectional.
# The display method shows each node and its neighbors along with the weights of the edges.
# The example at the end demonstrates how to create a weighted graph and display its structure.
# The graph is undirected, meaning edges are bidirectional.