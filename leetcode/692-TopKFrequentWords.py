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
        """
        freqDict = dict()
        for word in words:
            if word in freqDict:
                freqDict[word] += 1
            else:
                freqDict[word] = 1
        freqWords = sorted(freqDict, key=lambda w:(-freqDict[w],w))
        return freqWords[:k]
        
        