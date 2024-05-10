from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
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
            
            while have == need:
                if r-l+1 < resLen:
                    res = [l, r]
                    resLen = r-l+1
                #pop from left of window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l +=1
        return s[res[0]:res[1]+1] if resLen != float('inf') else ''