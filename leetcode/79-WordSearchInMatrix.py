class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
        Output: true
        """
        rows, cols = len(board), len(board[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

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
                if bfs(r,c):
                    return True
        return False