class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            w = r - l
            maxArea = max(maxArea, min(height[l], height[r]) * w)
            if height[l] <= height[r]:
                l = l +1
            else:
                r = r -1
        return maxArea