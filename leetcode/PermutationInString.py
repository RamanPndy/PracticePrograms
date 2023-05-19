from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        Get the character count, say c1, of the string s1.
        Get the character count, say c2, of the first n1 chars of s2, where n1, and n2 are lengths of s1 and s2 respectively.
        Use the sliding-window approach to slide c2 one character at a time to the right of s2
        After every slide, compare if c1 equals c2. If yes, we found a permutation of s1 in s2, hence return True, else continue.
        To avoid linear time comparision of c1 and c2, use a equality counter, say eq_count which keeps count of number of characters in c1 and c2 with equal counts. This reduces the comparision to constant time.
        """
        n1, n2 = len(s1), len(s2)
        c1, c2 = Counter(s1), Counter(s2[:n1])

        eq_count = sum([c1[ch] == c2[ch] for ch in c1])
        for i in range(n1,n2):
            if eq_count == len(c1):
                return True
            
            fst, lst = s2[i-n1], s2[i]
            if c1[lst] and c2[lst] == c1[lst]:
                eq_count -= 1
            c2[lst] += 1
            if c1[lst] and c2[lst] == c1[lst]:
                eq_count += 1
            
            if c1[fst] and c2[fst] == c1[fst]:
                eq_count -= 1
            c2[fst] += 1
            if c1[fst] and c2[fst] == c1[fst]:
                eq_count += 1
        return eq_count == len(c1)