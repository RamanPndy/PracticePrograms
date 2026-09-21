class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

        Connect: A cell is connected to adjacent cells horizontally or vertically.
        Region: To form a region connect every 'O' cell.
        Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
        To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.


        Example 1:

        Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

        Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

        Question:

        How can we efficiently capture all surrounded regions in the given board?
        Approach:
        - Traverse the border of the board and mark all 'O's connected to the border as safe (e.g., using a temporary marker like 'S').
        - After marking, traverse the entire board:
            - Convert all remaining 'O's to 'X's (these are the surrounded regions).
            - Convert all 'S's back to 'O's (these are the safe regions).
        - This approach ensures that only the 'O's completely surrounded by 'X's are captured, while the 'O's connected to the border remain unchanged.
        Edge Cases:
        - If the board is empty, do nothing.
        - If the board has only one row or one column, no 'O's can be surrounded, so they remain unchanged.
        - If the board contains only 'X's, no changes are needed.
        - If the board contains only 'O's, all 'O's on the border will be marked as safe, and the rest will be captured.
        - If the board contains a mix of 'X's and 'O's, only the 'O's completely surrounded by 'X's will be captured.

        Time Complexity: O(m * n), where m is the number of rows and n is the number of columns. Each cell is visited at most twice.
        Space Complexity: O(m * n) in the worst case due to the recursion stack used in the mark_safe function.
        Note:
        - The mark_safe function uses depth-first search (DFS) to traverse and mark all 'O's connected to the border as safe.
        - The approach modifies the board in-place, ensuring no additional space is used apart from the recursion stack.
        - This solution assumes that the input board is mutable and can be modified in-place.
        - The solution handles edge cases such as empty boards, single row/column boards, and boards with only 'X's or 'O's.
        - The solution ensures that only 'O's completely surrounded by 'X's are captured, while 'O's connected to the border remain unchanged.
        - The solution uses a temporary marker 'S' to differentiate between safe and capturable 'O's.

        Steps:
        1. Traverse the border of the board and mark all 'O's connected to the border as safe using the mark_safe function.
        2. Traverse the entire board and convert all remaining 'O's to 'X's and all 'S's back to 'O's.
        3. The board now correctly reflects all surrounded regions captured and safe regions preserved.
        4. Return from the function as the board is modified in-place.

        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def mark_safe(r, c):
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == 'O':
                board[r][c] = 'S'
                mark_safe(r+1, c)
                mark_safe(r-1, c)
                mark_safe(r, c+1)
                mark_safe(r, c-1)

        # Mark all 'O's connected to the border as safe
        for r in range(rows):
            mark_safe(r, 0)
            mark_safe(r, cols-1)
        for c in range(cols):
            mark_safe(0, c)
            mark_safe(rows-1, c)

        # Convert all remaining 'O's to 'X's and 'S's back to 'O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'

        def bfs(r, c):
            queue = [(r, c)]
            while queue:
                cr, cc = queue.pop(0)
                if 0 <= cr < rows and 0 <= cc < cols and board[cr][cc] == 'O':
                    board[cr][cc] = 'S'
                    queue.append((cr+1, cc))
                    queue.append((cr-1, cc))
                    queue.append((cr, cc+1))
                    queue.append((cr, cc-1))

        # You can use bfs instead of mark_safe if needed
        # for r in range(rows):
        #     bfs(r, 0)
        #     bfs(r, cols-1)
        # for c in range(cols):
        #     bfs(0, c)
        #     bfs(rows-1, c)