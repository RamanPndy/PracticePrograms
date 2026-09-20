class Solution(object):
    def generateParenthesis(self, n):
        """
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]
        1. The idea is to add ')' only after valid '('
        2. We use two integer variables left & right to see how many '(' & ')' are in the current string
        3. If left < n then we can add '(' to the current string
        4. If right < left then we can add ')' to the current string
        Question: Generate all combinations of well-formed parentheses given n pairs.
        Approach:
        - Use a queue to perform a breadth-first search (BFS) on all possible combinations.
        - Keep track of the number of left and right parentheses added so far.
        - Only add a left parenthesis if the number of left parentheses is less than n.
        - Only add a right parenthesis if the number of right parentheses is less than the number of left parentheses.
        - Continue until all combinations of length 2*n are generated.
        Time Complexity: O(4^n / sqrt(n)) as there are Catalan number of combinations.
        Space Complexity: O(4^n / sqrt(n)) for the queue and result storage.
        Steps:
        1.create left and right pointer with values 0 and append them into queue along with empty character
        2. create result array
        3. traverse queue
            - pop from queue and get left, right and current character from the queue
            - if len(current character) == n * 2 then append current character to result array
            - if left < n then increase left and append '(' to current character
            - if right < left then increase right and append ')' to current character
        4. return result array
        """
        l, r = 0, 0
        q = [(l, r, '')]
        res = []
        while q:
            l, r, c = q.pop()
            if len(c) == n * 2:
                res.append(c)
            if l < n:
                q.append((l +1, r, c + '('))
            if r < l:
                q.append((l, r + 1, c + ')'))
        return res