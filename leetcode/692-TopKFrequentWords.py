class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        Input: words = ["i","love","leetcode","i","love","coding"], k = 2
        Output: ["i","love"]
        Explanation: "i" and "love" are the two most frequent words.
        Note that "i" comes before "love" due to a lower alphabetical order.
        Question: What are the k most frequent words in the list, sorted by frequency and then alphabetically?
        Intuition:
        - We can use a dictionary to count the frequency of each word.
        - Sorting the words first by frequency (in descending order) and then alphabetically will give us the desired order.
        Approach:
        - Count the frequency of each word using a dictionary.
        - Sort the words based on frequency and alphabetical order.
        - Return the first k words from the sorted list.
        Steps:
        1. Initialize an empty dictionary to count word frequencies.
        2. Traverse the list of words and update the frequency count in the dictionary.
        3. Sort the words based on frequency (in descending order) and then alphabetically.
        4. Return the first k words from the sorted list.
        Time Complexity: O(n log n) where n is the number of unique words.
        Space Complexity: O(n) for the frequency dictionary.
        """
        freqDict = dict()
        for word in words:
            if word in freqDict:
                freqDict[word] += 1
            else:
                freqDict[word] = 1
        freqWords = sorted(freqDict, key=lambda w:(-freqDict[w],w))
        return freqWords[:k]
        
        