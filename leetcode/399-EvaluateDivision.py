from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
        Explanation: 
        Given: a / b = 2.0, b / c = 3.0
        queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
        return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
        """
        '''
        {"a" : [(2.0, "b")], "b": [(0.5,"a"), (3.0, "c")], "c": [(0.33, "b")] }
        c  = 0.33 * 3.0
        a = 2.0 
        a /c 
        Steps:
        1. Create a graph where each node represents a variable and edges represent the division relationships.
        2. For each query, perform a BFS or DFS to find the path from the numerator to the denominator.
        3. Multiply the edge weights along the path to get the result.
        4. If no path exists, return -1.0.
        Intuition: The problem can be solved by representing the equations as a graph and using BFS or DFS to find the division result for each query.
        Time Complexity: O(Q * (V + E)), where Q is the number of queries, V is the number of variables, and E is the number of equations.
        Space Complexity: O(V + E), for storing the graph and the visited set during BFS/DFS.
        Strategy: Represent the equations as a graph and use BFS or DFS to find the division result for each query.
        '''
        maps = defaultdict(dict)

        for (left, right), value in zip(equations, values):
            maps[left][right] = value
            maps[right][left] = 1/value

        results = []
        for left, right in queries:
            visited = set()
            q = [(left, 1)]  # node and the cost to get here
            res = -1
            while q:
                node, cost = q.pop(0)
                visited.add(node)
                # Check if the current node has a direct edge to the target node.
                if right in maps[node]:
                    res = cost * maps[node][right]
                    break
                # Add all unvisited neighbors to the queue with the updated cost.
                q.extend([(neighbor, cost * n_cost) for neighbor, n_cost in maps[node].items() if neighbor not in visited])
            results.append(res)

        return results