class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        TC: O(n * m * 4^L), where n and m are the dimensions of the board and L is the length of the word.
        SC: O(L), where L is the length of the word, due to the recursion stack in the DFS approach.

        Question: Can you determine if a given word exists in the 2D board by moving horizontally or vertically to adjacent cells?
        Approach:
        - Use a depth-first search (DFS) approach to explore all possible paths in the board.
        - Start from each cell and recursively check if the word can be formed by moving horizontally or vertically to adjacent cells.
        - Keep track of visited cells to avoid revisiting them in the current path.
        - Backtrack by unmarking the visited cells when returning from the recursive call.

        Steps:
        1. Define a helper function dfs(r, c, curr_char_in_target_word) to perform depth-first search.
        2. If the current character index reaches the length of the word, return True.
        3. Check boundary conditions, character match, and visited cells. If any condition fails, return False.
        4. Mark the current cell as visited and recursively explore all four directions.
        5. Unmark the current cell as visited (backtrack) and return the result of the recursive calls.
        6. Iterate through each cell in the board and call dfs starting from that cell.
        7. If any dfs call returns True, the word exists in the board; otherwise, return False.

        Example:
        Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
        Output: True
        Explanation: The word "ABCCED" can be formed by the path [(0,0),(0,1),(0,2),(1,2),(2,2),(2,1)] in the board.
        """
        rows, cols = len(board), len(board[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r,c,curr_char_in_target_word):
            if curr_char_in_target_word == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                word[curr_char_in_target_word] != board[r][c] or
                (r,c) in visited):
                return False
            visited.add((r,c))
            res= (dfs(r + 1, c, curr_char_in_target_word+1) or
            dfs(r - 1, c, curr_char_in_target_word+1) or
            dfs(r, c + 1, curr_char_in_target_word+1) or
            dfs(r, c - 1, curr_char_in_target_word+1))
            visited.remove((r,c))
            return res
        

        def bfs(row, col):
            """
            Breadth-first search (BFS) approach to explore all possible paths in the board starting from the given cell.
            - Use a queue to keep track of the current position, the letters collected so far, and the index of the current character in the target word.
            - Check boundary conditions, character match, and visited cells.
            - If the collected letters match the target word, return True.
            - Otherwise, continue exploring all four directions.
            - Return False if the word cannot be formed starting from the given cell.
            """
            q = [(row, col, word[0], 0)]
            while q:
                r, c, letter, i = q.pop(0)
                if i > len(word):
                    letter = letter[1:]

                # Remove the first character if the index exceeds the length of the word
                if i < len(word) and board[row][col] != word[i]:
                    continue

                # Check if the collected letters match the target word
                if letter == word:
                    return True
                visited.add((row, col))
                for dx, dy in directions:
                    r, c = r + dx,  c + dy
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                        q.append((r, c, letter + word[i+1], i+1))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c, 0):
                    return True
        return False
