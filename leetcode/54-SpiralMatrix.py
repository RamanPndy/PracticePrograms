class Solution(object):
    def spiralOrder(self, matrix):
        """
        Given an m x n matrix, return all elements of the matrix in spiral order.
        :type matrix: List[List[int]]
        :rtype: List[int]
        Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        Output: [1,2,3,6,9,8,7,4,5]

        Time complexity: O(m * n)
        Space complexity: O(1)

        Steps:
        1. in each iteration we will shrink boundaries of matrix
        2. we will start at top left position and move to right
        3. create result array
        4. create 4 vars representing left, right, top and bottom boundaries where top and left would be 0 and 
            right would be number of columns in matrix and bottom would be number of rows in matrix
            initially 
            top would point to top row of matrix
            bottom would point to last row of matrix
            left would point to left most column of matrix
            right would point to right most column of matrix
        5. while left < right and top < bottom
            - traverse top row from left to right and put element matrix[left][i] in result array
            - shrink top boundry by pushing to down ie. top += 1

            - traverse right most column by top to bottom and put element matrix[i][right -1] in result array
            - shrink right boundry by pushing to left ie. right -= 1

            - if not(left < right and top < bottom) then break. this case would be helpful for single dimension matrix

            - traverse bottom row from right to left and put element matrix[bottom - 1][i] in result array
            - shrink bottom boundry by pushing to up ie. bottom -= 1

            - traverse left most column by bottom to top and put element matrix[i][left] in result array
            - shrink left boundry by pushing to right ie. left += 1
        6. return result
        """
        res = []
        left, right = 0, len(matrix[0]) #num of columns
        top, bottom = 0, len(matrix) #num of rows

        while left < right and top < bottom:
            # get every i in top row
            for i in range(left, right):
                # top row
                res.append(matrix[left][i])
            # shrink top
            top += 1

            # get every i in right column
            for i in range(top, bottom):
                # right most column
                res.append(matrix[i][right -1])
            # shrink right
            right -= 1

            if not(left < right and top < bottom):
                break
            
            # get every i in bottom row
            for i in range(right-1, left-1, -1):
                # bottom row
                res.append(matrix[bottom-1][i])
            # shrink bottom
            bottom -= 1

            # get every i in left column
            for i in range(bottom -1, top -1, -1):
                # left most column
                res.append(matrix[i][left])
            # shrink left
            left += 1
        return res