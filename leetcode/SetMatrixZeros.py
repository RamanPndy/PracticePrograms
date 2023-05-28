class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m , n = len(matrix), len(matrix[0])
        first_row_has_zero , first_col_has_zero = False, False

        # iterate through matrix to mark the zero row and cols
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    if r == 0:
                        first_row_has_zero = True
                    if c == 0:
                        first_col_has_zero = True
                    matrix[r][0] = matrix[0][c] = 0
        
        # iterate through matrix to update the cell to be zero if it's in a zero row or col
        for r in range(1, m):
            for c in range(1, n):
                matrix[r][c] = 0 if matrix[r][0] == 0 or matrix[0][c] == 0 else matrix[r][c]
        
        # update the first row and col if they're zero
        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0
        
        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0