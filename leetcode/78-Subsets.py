'''
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''
class Solution:
    def subsets(self, nums):
        res = []
        subsets = []
        def dfs(i):
            if i >= len(nums):
                res.append(subsets[:])
                return
            
            #if we include nums[i]
            subsets.append(nums[i])
            dfs(i+1)

            #if we don't include nums[i]
            subsets.pop()
            dfs(i+1)
        dfs(0)
        return res