class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        Input: digits = "23"
        Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        """
        if not digits:
            return []

        m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        q = []
        q.append((0, ""))
        while q:
            i, s = q.pop(0)
            if i == len(digits):
                res.append(s)
            else:
                nextDigit = digits[i]
                letters = m[nextDigit]
                for letter in letters:
                    q.append((i+1, s + letter))
        return res