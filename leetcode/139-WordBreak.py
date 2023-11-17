class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        Input: s = "leetcode", wordDict = ["leet","code"]
        Output: true
        Explanation: Return true because "leetcode" can be segmented as "leet code".
        Steps:
        1. create a queue and append string in it.
        2. create a seen set which will store traversed word
        3. traverse q and get popped string
        4. traverse word list
            - if popped string starts with current word then create new word considering all the remaining character from the length of current word
            - if new word is empty then return true
            - if new word is not in seen set then append new word in queue and set.
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