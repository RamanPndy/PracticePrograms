class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        Input: s = "leetcode", wordDict = ["leet","code"]
        Output: true
        Explanation: Return true because "leetcode" can be segmented as "leet code".
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