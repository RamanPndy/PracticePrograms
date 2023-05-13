class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        lmx, rmx, tw = 0, 0, 0
        while l < r :
            if height[l] < height[r]:
                if height[l] > lmx:
                    lmx = height[l]
                else:
                    tw += lmx - height[l]
                l += 1
            else:
                if height[r] > rmx:
                    rmx = height[r]
                else:
                    tw += rmx - height[r]
                r -= 1
        return tw