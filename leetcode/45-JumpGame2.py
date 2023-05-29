class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Input: nums = [2,3,1,1,4]
        Output: 2
        Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, 
        then 3 steps to the last index.
        """
        cur_end, nxt_end = 0, 0
        steps = 0
        for i, n in enumerate(nums):
            if i > cur_end:
                steps += 1
                cur_end = nxt_end
            nxt_end = max(nxt_end, i + n)
        return steps