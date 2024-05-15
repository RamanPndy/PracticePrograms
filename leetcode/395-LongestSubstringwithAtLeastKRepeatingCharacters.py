from collections import defaultdict
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        Input: s = "aaabb", k = 3
        Output: 3
        Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
        1. First, we check if the length of the string is less than k. If so, we can immediately 
        return 0, since no substring of the string can have a frequency of each character greater than 
        or equal to k.
        2. Next, we count the frequency of each character in the string using a dictionary. We can do 
        this by iterating through each character in the string, and adding 1 to the corresponding 
        dictionary value each time we encounter the character.
        3. We then find the index of the first character in the string that has a frequency less than k. 
        If all characters have a frequency greater than or equal to k, we can immediately return the 
        length of the string.
        4. If we have found a character with a frequency less than k, we split the string into two 
        parts left and right viz
        left : substring before the current index
        right : substring after the current index. 
        We then recursively call the longestSubstring function on each substring to find the longest 
        substring in each part.
        5. Finally, we return the maximum length of the two substrings found in step 4.
        """
        if len(s) < k:
            return 0

        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        
        for i, c in enumerate(s):
            if freq[c] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i+1:], k)
                return max(left, right)
        
        return len(s)