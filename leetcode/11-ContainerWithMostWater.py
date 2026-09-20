class Solution(object):
    def maxArea(self, height):
        """
        You are given an integer array height of length n. 
        There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
        Find two lines that together with the x-axis form a container, such that the container contains the most water.
        Return the maximum amount of water a container can store.

        Notice that you may not slant the container.
        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
        In this case, the max area of water (blue section) the container can contain is 49.
        Question: Given an array of integers height representing the height of vertical lines, find the maximum area of water that can be contained between two lines.
        Approach:
        - Use a two-pointer approach, starting with one pointer at the beginning and one at the end of the array.
        - Calculate the area formed by the lines at the two pointers and update the maximum area.
        - Move the pointer pointing to the shorter line inward to potentially find a larger area.
        - Repeat until the pointers meet.
        Time Complexity: O(n) where n is the length of the array.
        Space Complexity: O(1) as we are using constant extra space.
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