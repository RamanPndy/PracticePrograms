class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        Input: matrix = [[1,-1],[-1,1]]
        Output: 4
        Explanation: We can follow the following steps to reach sum equals 4:
        - Multiply the 2 elements in the first row by -1.
        - Multiply the 2 elements in the first column by -1.

        Steps:
        1. get the count of negative numbers in matrix.
        2. get the minimum absolute number from matrix.
        3. traverse matrix
            1. if number is negative then increase negative count.
            2. add absolute number in the matrix sum.
            3. update minimum of matirx by absoulte number.
        4. if negative count is even then all numbers can be turned into positive in matrix and sumOfMatrix will be actual sum.
        5. if negative count is odd then only minimum number of the matrix can be turned into negative then twice of that number 
            can be subtracted from matrix sum which would be answer.
        """
        negativeCounts, sumOfMatrix = 0, 0
        minimumOfMatrix = float('inf')
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] < 0:
                    negativeCounts += 1
                sumOfMatrix += abs(matrix[i][j])
                minimumOfMatrix = min(minimumOfMatrix, abs(matrix[i][j]))
        if negativeCounts % 2 == 0:
            return sumOfMatrix
        else:
            return sumOfMatrix - (2*minimumOfMatrix)