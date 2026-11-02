class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        Question:
        Given a string s, sort it in decreasing order based on the frequency of characters.

        Example:
        Input: s = "tree"
        Output: "eert"
        Explanation: 'e' appears twice while 'r' and 't' appear once each.

        Approach:
        1. Count the frequency of each character using a dictionary.
        2. Sort the characters based on their frequency in descending order.
        3. Build the result string by repeating each character according to its frequency.

        Why this works:
        By counting the frequency and sorting accordingly, we ensure that characters with higher frequency appear first.

        Time complexity:
        O(n log n) where n is the length of the string due to sorting.

        Space complexity:
        O(n) for storing the frequency of characters.
        """
        from collections import Counter
        freq = Counter(s)
        return ''.join(char * times for char, times in sorted(freq.items(), key=lambda x: -x[1]))
        