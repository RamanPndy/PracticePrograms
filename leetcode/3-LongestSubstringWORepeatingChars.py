class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Given a string s, find the length of the longest substring without duplicate characters.
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
        s = "abcbxy"
        s2 = "abbxy"
        s3 = "abcba"
        s4 = "aaaa"
        s5 = "abcd"
        s6 = "abcdaxyz"
        Steps:
        1. if string is empty then return 0
        2. create 2 vars res and maxLen which will hold result string and it's length.
        3. traverse through string character by character 
            - if current character is not present in res then add it and update maxLen with len(res)
            - else split res on current character and append 1st splitted character along with current character in res.

        # Time: O(n)
        # Space: O(1)
        Question:

        How can we efficiently find the length of the longest substring without repeating characters in a given string?
        Approach:
        - Use a sliding window to keep track of the current substring without repeating characters.
        - Use a set to store the characters in the current window.
        - Expand the window by adding characters to the set until a duplicate is found.
        - When a duplicate is found, shrink the window from the left until the duplicate is removed.
        - Keep track of the maximum length of the window during the process.
        Edge Cases:
        - If the input string is empty, the result is 0.
        - If all characters in the string are unique, the result is the length of the string.
        - If all characters in the string are the same, the result is 1.
        - If the string contains multiple repeating characters, the algorithm should correctly identify the longest substring without duplicates.
        Example Walkthrough:

        For s = "abcabcbb", the longest substring without repeating characters is "abc" with length 3.
        For s = "abcbxy", the longest substring without repeating characters is "cbxy" with length 4.
        For s = "abbxy", the longest substring without repeating characters is "bxy" with length 3.
        For s = "abcba", the longest substring without repeating characters is "abc" with length 3.
        For s = "aaaa", the longest substring without repeating characters is "a" with length 1.
        For s = "abcd", the longest substring without repeating characters is "abcd" with length 4.
        For s = "abcdaxyz", the longest substring without repeating characters is "cdaxyz" with length 6.
        For s = "", the longest substring without repeating characters is "" with length 0.
        For s = "a", the longest substring without repeating characters is "a" with length 1.
        """
        res = ''
        maxLen = 1
        if not s:
            return 0
        for c in s:
            if c not in res:
                res += c
                maxLen = max(maxLen, len(res))
            else:
                # When a duplicate character is found, split the current result string on the duplicate character and keep the part after it, 
                # then append the current character.
                res = res.split(c)[1] + c
        # print (res)
        return maxLen