class Solution(object):
    def convert(self, s, numRows):
        """
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
        (you may want to display this pattern in a fixed font for better legibility)
        And then read line by line: "PAHNAPLSIIGYIR"
        
        Write the code that will take a string and make this conversion given a number of rows:
        string convert(string s, int numRows);

        Input: s = "PAYPALISHIRING", numRows = 3
        Output: "PAHNAPLSIIGYIR"
        Question: Given a string s and an integer numRows, convert the string into a zigzag pattern on the given number of rows and then read it line by line.
        Approach:
        - Create a list of lists to represent each row.
        - Use an index to keep track of the current row and a step to determine the direction of traversal.
        - Traverse each character in the string and append it to the appropriate row.
        - Change the direction when the first or last row is reached.
        - Combine all characters from each row to form the final string.
        Time Complexity: O(n) where n is the length of the string.
        Space Complexity: O(n) for storing the characters in the rows.
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