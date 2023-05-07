#Breadth First Search
class Vertex:
    def __init__(self,n):
        self.name = n
        self.neighbours = list()

        self.distance = 9999
        self.color = 'black'#unvisited

    def add_neighbour(self,v):
        if v not in self.neighbours:
            self.neighbours.append(v)
            self.neighbours.sort()

class Graph:
    vertices = {}

    def add_vertix(self,vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self,u,v):
        if u in self.vertices and v in self.vertices:
            for key,value in self.vertices.items():
                if key == u:
                    value.add_neighbour(v)
                elif key == v :
                    value.add_neighbour(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbours) + " "+self.vertices[key].distance)

    def bfs(self,vert):
        q = list()
        vert.distance = 0
        vert.color = 'red'
        for v in vert.neighbours:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)

        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'

            for v in node_u.neighbours:
                node_v = self.vertices[v]
                if node_v.color == 'black':
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1



