class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
        Steps:
        1. 2 pointer approach, set l=0 and r=len(height) -1 and maxArea =0
        2. traverse while left < right
            - weight = right -left
            - update maxArea by min(height(left), height(right)) * weight
        3. if height(left) < height(right) then increase left otherwise decrease right
        4. return calculated maxArea
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