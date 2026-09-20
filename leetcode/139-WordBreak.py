class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        Input: s = "leetcode", wordDict = ["leet","code"]
        Output: true
        Explanation: Return true because "leetcode" can be segmented as "leet code".
        Question: Determine if the string s can be segmented into a space-separated sequence of one or more dictionary words from wordDict.
        Approach:
        - Use a queue to perform a breadth-first search (BFS) on the string.
        - Keep track of visited substrings to avoid redundant work.
        - For each substring, check if it starts with any word in the dictionary.
        - If it does, create a new substring by removing the matched word and continue the process.
        - If an empty substring is reached, return True.
        - If the queue is exhausted without finding an empty substring, return False.
        Example:
        Input: s = "leetcode", wordDict = ["leet","code"]
        Output: true
        Explanation: Return true because "leetcode" can be segmented as "leet code".
        Another Example:

        Input: s = "applepenapple", wordDict = ["apple","pen"]
        Output: true
        Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
        Another Example:

        Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
        Output: false
        Explanation: Return false because "catsandog" cannot be segmented into a sequence of dictionary words.
        Time : O(n * m * k) where n is the length of the string, m is the number of words in the dictionary, and k is the average length of the words.
        Space: O(n) for the queue and seen set.
        Steps:
        1. create a queue and append string in it.
        2. create a seen set which will store traversed word
        3. traverse q and get popped string
        4. traverse word dictionary
            - if popped string starts with current word then create new word considering all the remaining character from 
                the length of current word
            - if new word is empty then return true
            - if new word is not in seen set then append new word in queue and seen set.
        5. default return false
        """
        q = [s]
        seen = set()
        while q:
            s = q.pop(0)
            for word in wordDict:
                if s.startswith(word):
                    newWord = s[len(word):]
                    if newWord == "":
                        return True
                    if newWord not in seen:
                        q.append(newWord)
                        seen.add(newWord)
        return False