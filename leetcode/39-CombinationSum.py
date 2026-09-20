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
        Question: Find all unique combinations of candidates where the chosen numbers sum to the target. Each number in candidates may be used an unlimited number of times.
        Approach:
        - Use a stack to keep track of the current combination and the remaining target.
        - Sort the candidates to facilitate pruning.
        - Use a set to quickly check if a number is a candidate.
        - Iterate through the stack, updating the current combination and remaining target.
        - Add valid combinations to the result list.
        Time Complexity: O(2^n) in the worst case, where n is the number of candidates.
        Space Complexity: O(n) for the stack.
        Steps:
        1. create a result array and todo stack and append (target, 0, combination stack([])) in stack
        2. sort candidates
        3. create pool of unique candidates ie. set of candidates
        4. if target present in the pool then append in result array
        5. traverse todo stack:
            - get current number, index and combination stack from popping todo stack
            - if current number is < value of candidate at index then continue
            - if current number is not equal to target and but present in the pool then add current number to 
              combination stack and append it to result array
            - while index is < len(candidates) and current number is >= value of candidate at index
              create temp stack and add candidate at current index and extend with combination stack
              then append ((current number - value of candidate at current index), index ,temp stack)
              increase index value by 1
        6. return result array
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
            
