from collections import defaultdict

class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        Input: s = "acfgbd", k = 2
        Output: 4
        Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
        Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.
        Question: What is the length of the longest ideal subsequence in the given string?
        Intuition:
        - We can use dynamic programming to keep track of the longest ideal subsequence ending with each character.
        Time Complexity: O(n * 26) where n is the length of the string and 26 is the number of lowercase letters.
        Space Complexity: O(26) for the dp map.
        Approach:
        - Use a dictionary to store the length of the longest ideal subsequence ending with each character.
        - For each character in the string, check all previous characters in the dictionary.
        - If the difference between the ASCII values of the current and previous character is less than or equal to k, update the length.
        - Finally, return the maximum length from the dictionary.
        Steps:
        1. create dp of map of int
        2. traverse string by character:
            - set newval as 0
            - traverse dp map
                - if difference of ascii values of current and previous character is <= k
                    then update newval as max of newval and dp[previous character]
            - dp[current character] = newval + 1
        3. return max of dp map values
        """
        dp = defaultdict(int)
        for ch in s:
            newval = 0
            for prev in dp:
                if abs(ord(prev) - ord(ch)) <= k:
                    newval = max(newval, dp[prev])
            dp[ch] = newval + 1
        return max(dp.values())