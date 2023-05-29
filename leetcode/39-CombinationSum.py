class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        Input: candidates = [2,3,6,7], target = 7
        Output: [[2,2,3],[7]]
        Explanation:
        2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
        7 is a candidate, and 7 = 7.
        These are the only two combinations.
        """
        res = []
        todo = [(target, 0, [])]
        candidates.sort()
        pool = set(candidates)
        if target in pool:
            res.append([target])
        while todo:
            curr, i, combis = todo.pop()
            if curr < candidates[i]:
                continue
            if curr != target and curr in pool:
                res.append(combis + [curr])
            while i < len(candidates) and curr >= candidates[i]:
                todo.append((curr - candidates[i], i, combis + [candidates[i]]))
                i += 1
        return res
            
