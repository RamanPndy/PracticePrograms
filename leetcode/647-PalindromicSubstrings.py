class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        Manacher’s algorithm:
        Input: s = "abc"
        Output: 3
        Explanation: Three palindromic strings: "a", "b", "c".
        Question: Count all palindromic substrings in the given string.
        Intuition: Expand around each character (and each pair of characters) to find all palindromic substrings.
        Steps:
        1. Define a helper function to expand around a given center and count palindromes.
        2. Iterate through each character in the string, treating it as the center of odd-length palindromes.
        3. Also consider each pair of consecutive characters as the center of even-length palindromes.
        4. Sum the counts from all centers to get the total number of palindromic substrings.
        Time Complexity: O(n^2), where n is the length of the string, as we expand around each center.
        Space Complexity: O(1), as we use only a constant amount of extra space.
        """
        def expandAndCountPallindromes(i, j, s):
            '''
            Counts the number of pallindrome substrings from a given center i,j        
            1. when i=j, it's an odd-lengthed pallindrome string. 
                eg: for string "aba", i=j=1.
            2. when i+1=j, it's an even-lengthed pallindrome string. 
                eg: for string "abba", i=1, j=2.
            '''
            l = len(s)
            cnt = 0
            while i >=0 and j < l and s[i] == s[j]:
                i -= 1
                j += 1
                cnt += 1
            return cnt
        
        res = 0
        for i in range(len(s)):
            # Count odd-length palindromes centered at i and even-length palindromes centered between i and i+1
            res += expandAndCountPallindromes(i, i, s) + expandAndCountPallindromes(i, i+1, s)
        return res