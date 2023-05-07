def topKFrequent(words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    freqDict = dict()
    for word in words:
        if word in freqDict:
            freqDict[word] += 1
        else:
            freqDict[word] = 1
    print (freqDict)

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2