from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"

        Question: Can you find the minimum window substring in s that contains all characters of t?
        Approach:
        - Use a sliding window with two pointers (left and right) to traverse the string s.
        - Maintain a frequency map for characters in t and a window frequency map for the current window in s.
        - Expand the window by moving the right pointer and update the window frequency map.
        - When the window contains all characters of t, try to shrink it from the left to find the minimum window.
        - Keep track of the minimum window length and its starting index.
        - Return the minimum window substring or an empty string if no such window exists.
        Time complexity: O(n + m), where n is the length of s and m is the length of t, as we traverse the string s once and maintain frequency maps.
        Space complexity: O(n + m), as we use frequency maps to store the characters of t and the current window in s.

        Steps:
        1. Initialize frequency maps for t and the current window in s.
        2. Use two pointers to represent the sliding window and variables to track the number of characters matched, 
            the minimum window length, and the starting index of the minimum window.
        3. Expand the window by moving the right pointer and updating the window frequency map.
        4. When the window contains all characters of t, try to shrink it from the left to find the minimum window.
        5. Update the minimum window length and starting index whenever a smaller valid window is found.
        6. Return the minimum window substring or an empty string if no such window exists.

        Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
        1. Check if s is shorter than t. If it is, there is no possible solution, and we return an empty string.
        2. Create a frequency map of characters in t.
        3. Initialize have, need, min_length, and l to 0.
        4. Traverse the string s using the end pointer.
        5. If the current character in s is present in the frequency map and character count in current window and 
            frequence map is same then increment the have.
        6. while have equals the need, it means we have found a window that contains all characters of t. 
          - Now we try to shrink the window by moving the left pointer forward until the window still contains all 
            the characters of t.
          - If the length of the current window is smaller than the minimum length so far, update the minimum length and the minimum start.
          - decrement character count from the current window for the left pointer.
          - if frequency of character at left in current window is less than from frequency map of t then decrement "have".
          - increment left pointer
        7.Return the minimum window or an empty string if no window exists.
        """
        if not t: return ""

        countT, window = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] += 1
        
        res = []
        resLen = float('inf')
        l = 0 
        have, need = 0, len(countT)
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if c in countT and window[c] == countT[c]:
                have += 1

            # try to shrink the window from the left while it still contains all characters of t
            while have == need:
                if r-l+1 < resLen:
                    res = [l, r]
                    resLen = r-l+1
                #pop from left of window
                window[s[l]] -= 1

                # move the left pointer to shrink the window
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l +=1
        return s[res[0]:res[1]+1] if resLen != float('inf') else ''