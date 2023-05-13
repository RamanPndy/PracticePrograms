class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
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