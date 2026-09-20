class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        Question:
        Rotate the given n x n 2D matrix by 90 degrees (clockwise) in-place.
        
        Approach:
        - First, reverse the matrix upside down.
        - Then, transpose the matrix by swapping matrix[i][j] with matrix[j][i] for all i and j.
        
        Complexity Analysis:
        - Time: O(n^2) because we traverse all elements of the matrix twice.
        - Space: O(1) since the rotation is done in-place.

        Steps:
        1. Reverse the matrix upside down.
        2. Transpose the matrix by swapping matrix[i][j] with matrix[j][i] for all i and j.
        
        """
        #reverse
        l, r = 0, len(matrix) -1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        
        #transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]