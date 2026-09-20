class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        Input: s = "bbbab"
        Output: 4
        Explanation: One possible longest palindromic subsequence is "bbbb".
        Question: Find the length of the longest palindromic subsequence in the given string.
        Intuition: The longest palindromic subsequence problem can be transformed into finding the longest common subsequence between the string and its reverse.
        Steps:
        1. Reverse the input string to get t.
        2. Initialize a 2D DP array of size (n+1) x (n+1) with all elements as 0.
        3. Traverse through both strings and fill the DP table using the LCS logic.
        4. Return the value at dp[n][n] as the length of the longest palindromic subsequence.
        Time Complexity: O(n^2), where n is the length of the input string, due to the nested loops for filling the DP table.
        Space Complexity: O(n^2), as we are using a 2D DP array of size (n+1) x (n+1).
        """
        n = len(s)
        t = s[::-1]
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][n]