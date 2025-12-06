from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.
        Input: strs = ["eat","tea","tan","ate","nat","bat"]

        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

        Explanation:

        There is no string in strs that can be rearranged to form "bat".
        The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
        The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
        """
        res = defaultdict(list)
        for s in strs:
            t = ''.join(sorted(s))
            res[t].append(s)
        return res.values()