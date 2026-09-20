from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        Input: s1 = "ab", s2 = "eidbaooo"
        Output: true
        Explanation: s2 contains one permutation of s1 ("ba").
        Get the character count, say c1, of the string s1.
        Get the character count, say c2, of the first n1 chars of s2, where n1, and n2 are lengths of s1 and s2 respectively.
        Use the sliding-window approach to slide c2 one character at a time to the right of s2
        After every slide, compare if c1 equals c2. If yes, we found a permutation of s1 in s2, hence return True, else continue.
        To avoid linear time comparision of c1 and c2, use a equality counter, say eq_count which keeps count of number of 
        characters in c1 and c2 with equal counts. This reduces the comparision to constant time.
        Question: Determine if s2 contains any permutation of s1.
        Intuition: Use a sliding window and character count comparison to efficiently check for permutations.
        Steps:
        1. Calculate the character count for s1 and the first window of s2.
        2. Initialize the equality counter.
        3. Slide the window over s2, updating the character count and equality counter.
        4. If at any point the equality counter matches the number of unique characters in s1, return True.
        5. If the loop ends without finding a match, return False.
        Time Complexity: O(n2), where n2 is the length of s2, as we traverse the array once with a sliding window.
        Space Complexity: O(n1), where n1 is the length of s1, as we store character counts for s1 and the current window in s2.
        Note: The equality counter optimization helps in reducing the comparison of character counts to constant time per window slide.
        """
        n1, n2 = len(s1), len(s2)
        c1, c2 = Counter(s1), Counter(s2[:n1])

        # Initialize the equality counter based on the initial window
        eq_count = sum([c1[ch] == c2[ch] for ch in c1])
        for i in range(n1,n2):
            if eq_count == len(c1):
                return True

            # Slide the window: remove the first character of the previous window and add the new character at the end of the current window
            fst, lst = s2[i-n1], s2[i]
            if c1[lst] and c2[lst] == c1[lst]:
                eq_count -= 1
            c2[lst] += 1
            if c1[lst] and c2[lst] == c1[lst]:
                eq_count += 1
            
            # Remove the first character of the previous window from the equality counter and update c2
            if c1[fst] and c2[fst] == c1[fst]:
                eq_count -= 1
            c2[fst] += 1
            if c1[fst] and c2[fst] == c1[fst]:
                eq_count += 1
        return eq_count == len(c1)