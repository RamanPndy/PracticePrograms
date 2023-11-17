class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        Input: s = "PAYPALISHIRING", numRows = 3
        Output: "PAHNAPLSIIGYIR"
        steps:
        1. first create 2D array of numRows
        2. create variables index = 0 and step = 1
        3. traverse through each character in string
            - append each character in each row by index
            - if index == 0 means first row then set step = 1
            - if index == numRows -1 means last row then set step = -1
            - add step for each index that way oscillation will happend
        4. combine all characters in each row so that rows become single list
        5. return final list as string
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for i in range(numRows)]
        index = 0
        step = 1
        for c in s:
            rows[index].append(c)
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)