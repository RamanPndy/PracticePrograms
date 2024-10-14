class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        TC: O(n * m * )
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
            q = [(row, col, word[0], 0)]
            while q:
                r, c, letter, i = q.pop(0)
                if i > len(word):
                    letter = letter[1:]
                if i < len(word) and board[row][col] != word[i]:
                    continue
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
