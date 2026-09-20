from collections import defaultdict

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        Input: s = "cbaebabacd", p = "abc"
        Output: [0,6]
        Explanation:
        The substring with start index = 0 is "cba", which is an anagram of "abc".
        The substring with start index = 6 is "bac", which is an anagram of "abc".
        Question:
        Find all start indices of p's anagrams in s.
        Approach:
        - Use a sliding window of size equal to the length of p.
        - Maintain frequency counts of characters in the current window and in p.
        - Compare the frequency counts to determine if the current window is an anagram of p.
        Time: O(n) where n is the length of s, as we iterate through the string once.
        Space: O(1) since the frequency maps have a fixed size of at most 26 for lowercase English letters.
        Steps:
        1. This can be solved with sliding window approach.
        2. create separate frequency map for both strings and pattern.
        3. create res array which will hold starting index of the anagram.
        4. if both frequency map is equal then put index 0 in the res arrray.
        5. set left pointer to 0 and traverse using right pointer from len(p) to len(s)
            - get left and right chanracter
            - in string frequency map
                - increase right character frequency count
                - reduce left character frequency count
                - if left frequency count becomes 0 then delete left character from frequency map
            - increase left pointer
            - at the point where both frequencies becomes equal then append left pointer to result array/
        6. return result array

        """
        if len(p) > len(s):
            return []
        m = defaultdict(int)
        n = defaultdict(int)

        for i in range(len(p)):
            m[p[i]] += 1
            n[s[i]] += 1
        
        res = [0] if m == n else []
        l = 0
        for r in range(len(p), len(s)):
            n[s[r]] += 1
            n[s[l]] -= 1

            if n[s[l]] == 0:
                del n[s[l]]
            l += 1
            if m == n :
                res.append(l)
        return res
        