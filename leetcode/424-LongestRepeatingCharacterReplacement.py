class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        Input: s = "ABAB", k = 2
        Output: 4
        Explanation: Replace the two 'A's with two 'B's or vice versa.
        Question: Find the length of the longest substring containing the same letter you can get after performing at most k replacements.
        Intuition: Use a sliding window approach to find the longest substring where we can replace at most k characters to make all characters the same. 
        Keep track of the frequency of characters within the window and adjust the window size based on the allowed replacements.
        Steps:
        1. Initialize a dictionary to keep track of character frequencies within the current window.
        2. Use two pointers to represent the sliding window.
        3. Expand the window by moving the right pointer and update the character frequencies.
        4. If the number of characters to replace exceeds k, shrink the window from the left.
        5. Keep track of the maximum window size that satisfies the condition.
        6. Return the maximum window size as the result.
        Time Complexity: O(n), where n is the length of the string, as each character is processed at most twice.
        Space Complexity: O(1), as the dictionary will contain at most 26 entries for uppercase English letters.
        """
        ans = 0
        freq = dict()
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in freq:
                v = freq[c]
                freq[c] = v+1
            else:
                freq[c] = 1

            max_repeated_char_count = max(freq.values())

            while r -l +1 - max_repeated_char_count > k:
                left_char = s[l]
                freq[left_char] -= 1
                l += 1
            ans = max(ans, r- l +1)
        return ans
        