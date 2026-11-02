class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        Question:
        Given a triangle array, return the minimum path sum from top to bottom. 
        Each step you may move to adjacent numbers on the row below.

        Example:
        Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
        Output: 11
        Explanation: The minimum path sum is 2 + 3 + 5 + 1 = 11.

        Approach:
        Use dynamic programming to calculate the minimum path sum from the bottom to the top.
        1. Start from the second last row and move upwards.
        2. For each element, add the minimum of the two adjacent elements from the row below.
        3. The top element will contain the minimum path sum.

        Why this works:
        By calculating the minimum path sum from the bottom to the top, we ensure that each element contains the minimum sum to reach the bottom, leading to the overall minimum path sum at the top.

        Time complexity:
        O(n) where n is the total number of elements in the triangle.

        Space complexity:
        O(1) if we modify the triangle in-place, otherwise O(n) for extra space.
        """
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]