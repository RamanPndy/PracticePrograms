
import collections
# Time: O(n)
# Space: O(n)
class Solution:
  """
      Question: Determine if the given edges form a valid tree with n nodes.
      Approach:
        - A valid tree with n nodes must have exactly n-1 edges.
        - Use BFS to traverse the graph starting from node 0.
        - Keep track of visited nodes to ensure all nodes are connected.
        - If all nodes are visited and the number of edges is n-1, it is a valid tree.
        Time: O(n) because we traverse all nodes and edges once.
        Space: O(n) for the graph representation and the queue used in BFS.
        Example:
        Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
        Output: True
        Explanation: The given edges form a valid tree with 5 nodes.

        Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
        Output: False
        Explanation: The given edges contain a cycle, so it is not a valid tree.
        Intuition:
          - A valid tree must be connected and acyclic.
          - The number of edges must be exactly n-1 for n nodes.
          - BFS can be used to check connectivity efficiently.
          - The combination of checking the number of edges and using BFS ensures both acyclicity and connectivity.
          - This approach leverages the properties of trees to efficiently determine validity.
        Algorithm:
          - Check if the number of edges is exactly n-1.
          - Build the graph using an adjacency list.
          - Use BFS to traverse the graph starting from node 0.
          - Keep track of visited nodes.
          - If all nodes are visited, return True; otherwise, return False.
        Complexity Analysis:
          - Time: O(n) because we traverse all nodes and edges once.
          - Space: O(n) for the graph representation and the queue used in BFS.
  """
  def validTree(self, n: int, edges):
    if n == 0 or len(edges) != n - 1:
      return False

    graph = [[] for _ in range(n)]
    q = collections.deque([0])
    seen = {0}

    for u, v in edges:
      graph[u].append(v)
      graph[v].append(u)

    while q:
      u = q.popleft()
      for v in graph[u]:
        if v not in seen:
          q.append(v)
          seen.add(v)

    return len(seen) == n
