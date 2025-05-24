import heapq

def prim(graph, start):
    '''
    Prim's algorithm to find the Minimum Spanning Tree (MST) of a connected, undirected graph.
    The graph is represented as an adjacency list where each node points to a list of tuples (neighbor, weight).
    TC: O((V + E) log V) where V is the number of vertices and E is the number of edges
    SC: O(V) for storing the MST and visited nodes
    '''
    # Initialize the MST and visited nodes
    # graph is a dict: node -> list of (neighbor, weight)
    mst = []  # list of edges in MST (node1, node2, weight)
    visited = set([start])
    edges = []

    # Add all edges from the start node to the priority queue
    for neighbor, weight in graph[start]:
        heapq.heappush(edges, (weight, start, neighbor))

    while edges:
        weight, node1, node2 = heapq.heappop(edges)
        if node2 not in visited:
            visited.add(node2)
            mst.append((node1, node2, weight))

            for next_neighbor, next_weight in graph[node2]:
                if next_neighbor not in visited:
                    heapq.heappush(edges, (next_weight, node2, next_neighbor))

    return mst

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

start_node = 'A'
mst = prim(graph, start_node)

print("Edges in MST:")
for edge in mst:
    print(edge)
