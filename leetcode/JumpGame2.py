class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_end, nxt_end = 0, 0
        steps = 0
        for i, n in enumerate(nums):
            if i > cur_end:
                steps += 1
                cur_end = nxt_end
            nxt_end = max(nxt_end, i + n)
        return steps