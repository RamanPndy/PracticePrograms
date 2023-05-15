from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        '''
        {"a" : [(2.0, "b")], "b": [(0.5,"a"), (3.0, "c")], "c": [(0.33, "b")] }
        c  = 0.33 * 3.0
        a = 2.0 
        a /c 
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
                if right in maps[node]:
                    res = cost * maps[node][right]
                    break
                q.extend([(neighbor, cost * n_cost) for neighbor, n_cost in maps[node].items() if neighbor not in visited])
            results.append(res)

        return results