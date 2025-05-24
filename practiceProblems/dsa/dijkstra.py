import heapq

def dijkstra(graph, start):
    '''
    Dijkstra's algorithm to find the shortest path from a start node to all other nodes in a weighted graph.
    The graph is represented as an adjacency list where each node points to a list of tuples (neighbor, weight).
    TC: O((V + E) log V) where V is the number of vertices and E is the number of edges
    SC: O(V) for storing distances
    '''
    # Initialize distances from start node to all other nodes as infinity
    # and distance to start node as 0
    # graph is a dict: node -> list of (neighbor, weight)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If this distance is not up to date, skip
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If shorter path found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

print(shortest_distances)
# Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
