class Solution(object):
    def trap(self, height):
        """
        Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
        In this case, 6 units of rain water (blue section) are being trapped.
        Question: How much water can be trapped after raining?
        Approach:
        - Use two pointers, one starting from the left and the other from the right.
        - Keep track of the maximum height encountered from both ends.
        - Calculate the trapped water at each position based on the difference between the current height and the maximum height from the respective side.
        - Move the pointers inward and update the total trapped water accordingly.
        Time Complexity: O(n) where n is the number of elements in the height array.
        Space Complexity: O(1) as we are using only a constant amount of extra space.
        Steps:
        - Initialize two pointers, `l` and `r`, at the start and end of the height array.
        - Initialize two variables, `lmx` and `rmx`, to keep track of the maximum height encountered from the left and right, respectively.
        - Initialize a variable `tw` to store the total trapped water.
        - While `l` is less than `r`, compare the heights at the two pointers and update the trapped water accordingly.
        - Move the pointers inward and update the maximum heights.
        - Return the total trapped water.
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