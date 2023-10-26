class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
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