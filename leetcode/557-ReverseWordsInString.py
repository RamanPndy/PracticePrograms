class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        Question: Reverse the order of words in the given string.
        Approach:
        1. Split the string by spaces to get individual words.
        2. Reverse the list of words.
        3. Join the reversed list with spaces to form the final string.

        Why this works: By splitting and reversing the words, we effectively reverse the order of words while 
        preserving the characters within each word.

        Time Complexity: O(n) where n is the length of the string.
        Space Complexity: O(n) for storing the split words and the reversed list.
        """
        words = s.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)
        