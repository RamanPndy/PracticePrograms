class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        Input: s = "12"
        Output: 2
        Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
        this is a fibonacci dp question and a bottom up dp question
        Loop through s (i)
        if s[i] is a valid number (not 0) then we can include the previous permutation (s[i+1] permutation)
        if s[i] can be expressed as 10-26 then we include previous previous permutation (s[i+2] permutation)
        Note: it is s[i+1] because we are going reverse
        return the last permutation
        dp[i] = dp[i+1] + dp[i+2]

        Question: Can you determine the number of ways to decode a given string of digits into letters, where 'A' = 1, 'B' = 2, ..., 'Z' = 26?
        Approach:
        - Use dynamic programming (DP) to solve the problem in a bottom-up manner.
        - Create a DP map to store the number of ways to decode substrings starting from each index.
        - Traverse the string in reverse order and calculate the number of ways to decode each substring based on single-digit and double-digit possibilities.
        - Return the number of ways to decode the entire string, which is stored in dp[0].
        Time Complexity: O(n), where n is the length of the input string s.
        Space Complexity: O(n), due to the DP map storing the number of ways to decode substrings.
        Steps:
        1. create dp map and intialize it with len(s):1 because if we get empty string then we will return 1. (base case)
        2. in bottom up approach traverse string in reverse order by index.
        3. if first character is 0 then we return 0 (base case)
        4. if it is not 0 then it means next number is between 1-9 then we can take this value as single digit 
            then subproblem becomes i+1
        5. check for double digit character if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")) then 
            subproblemn becomes i+2
        6. return dp[0]
        """
        dp = {len(s) : 1}

        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

            # Check for valid two-digit decode possibilities and update dp[i] accordingly.
            if (i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                dp[i] += dp[i+2]
        return dp[0]