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

        Question: Can you solve this problem in O(m * n) time complexity and O(1) space complexity?
        Approach:
        - Use four pointers to represent the boundaries of the matrix: top, bottom, left, and right.
        - Traverse the matrix in a spiral order by moving right, down, left, and up while shrinking the boundaries.
        - Append each element to the result array during the traversal.
        - Continue the traversal until the boundaries overlap.
        - Return the result array containing the elements in spiral order.

        Time complexity: O(m * n), where m is the number of rows and n is the number of columns.
        Space complexity: O(1), as we are using only a constant amount of extra space.
        Notes:
        - The algorithm uses four pointers to keep track of the current boundaries of the matrix.
        - By shrinking the boundaries after traversing each side, we ensure that each element is visited exactly once.
        - The check `if not(left < right and top < bottom)` is necessary to handle single row or single column remaining in the matrix.
        - The algorithm ensures that each element is added to the result array exactly once.
        - The boundaries are adjusted after traversing each side to avoid revisiting elements.
        - This approach allows us to traverse the matrix in a spiral order without using additional space for visited elements.
        - The algorithm works for both square and rectangular matrices.
        - The algorithm handles edge cases such as empty matrices gracefully.

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