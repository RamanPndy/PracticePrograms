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

        Question: Can you solve this problem in O(n * k log k) time complexity, where n is the number of strings and k is the maximum length of a string?
        Approach:
        - Use a dictionary to group strings by their sorted version.
        - Iterate through each string in the input list.
        - Sort the string and use it as a key in the dictionary.
        - Append the original string to the list corresponding to the sorted key.
        - Return the values of the dictionary as the grouped anagrams.
        Time complexity: O(n * k log k), where n is the number of strings and k is the maximum length of a string.
        Space complexity: O(n * k), where n is the number of strings and k is the maximum length of a string.
        Steps:
        1. Initialize a defaultdict to store lists of anagrams.
        2. Iterate through each string in the input list.
        3. Sort the string and use it as a key in the dictionary.
        4. Append the original string to the list corresponding to the sorted key.
        5. Return the values of the dictionary as the grouped anagrams.
        """
        res = defaultdict(list)
        for s in strs:
            t = ''.join(sorted(s))
            res[t].append(s)
        return res.values()