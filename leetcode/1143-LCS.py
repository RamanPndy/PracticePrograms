class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        Input: text1 = "abcde", text2 = "ace" 
        Output: 3  
        Explanation: The longest common subsequence is "ace" and its length is 3.

        Question: What is the length of the longest common subsequence between text1 and text2?
        Intuition: The longest common subsequence can be found using dynamic programming by comparing characters of both strings and building up a 
        solution for increasing lengths of substrings.
        Steps:
        1. Initialize a 2D array dp with dimensions (m+1) x (n+1) filled with zeros, where m and n are the lengths of text1 and text2 respectively.
        2. Iterate through each character of text1 and text2.
        3. If the characters match, set dp[i][j] = 1 + dp[i-1][j-1].
        4. If the characters do not match, set dp[i][j] = max(dp[i-1][j], dp[i][j-1]).
        5. The value at dp[m][n] will be the length of the longest common subsequence.
        Time Complexity: O(m * n), where m and n are the lengths of text1 and text2.
        Space Complexity: O(m * n) for the dp array.
        Interview Explanation: The key insight is to use dynamic programming to build up the solution for the longest common subsequence by 
        comparing characters and using previously computed results to avoid redundant calculations.
        """
        m, n = len(text1), len(text2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        ans = 0
        for i in range(1,m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                ans = max(ans, dp[i][j])
        return ans