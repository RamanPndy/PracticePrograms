class Graph:
    '''
    A class to represent a directed graph using adjacency list representation.
    Supports adding edges and checking for cycles using DFS.
    TC: O(V + E) for cycle detection (V = vertices, E = edges)
    SC: O(V) for visited and recursion stack arrays
    '''
    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, src, dest):
        if src not in self.adj_list:
            self.add_vertex(src)
        if dest not in self.adj_list:
            self.add_vertex(dest)

        self.adj_list[src].append(dest)

        if not self.directed:
            self.adj_list[dest].append(src)

    def remove_edge(self, src, dest):
        if src in self.adj_list and dest in self.adj_list[src]:
            self.adj_list[src].remove(dest)
        if not self.directed and dest in self.adj_list and src in self.adj_list[dest]:
            self.adj_list[dest].remove(src)

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            del self.adj_list[vertex]
        for v in self.adj_list:
            if vertex in self.adj_list[v]:
                self.adj_list[v].remove(vertex)

    def display(self):
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex} -> {neighbors}")

g = Graph(directed=False)
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")

g.display()
