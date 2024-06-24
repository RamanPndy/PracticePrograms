class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        Input: s = "ABAB", k = 2
        Output: 4
        Explanation: Replace the two 'A's with two 'B's or vice versa.
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
        