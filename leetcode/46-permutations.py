class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Input: nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        Steps:
        1. create result array which will hold all possible permutations
        2. if len(nums) == 1 ie. there is only 1 element in nums array then return all of the elements from nums array
        3. traverse nums array by index:
            - pop out number from nums array at index 0
            - do recursion on remaining numbers and assign results of that to temp stack
            - traverse temp stack
                - put popped number in temp stack
            - extend temp stack in result array
            - put back number in nums array
        4. return result
        """
        res = []
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res