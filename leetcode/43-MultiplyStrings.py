class Solution(object):
    def multiply(self, num1, num2):
        """
        Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

        Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
        Input: num1 = "2", num2 = "3"
        Output: "6"
        Question: What is the product of num1 and num2 represented as a string?
        Approach:
        - Convert each character of the input strings to its corresponding integer value.
        - Multiply the resulting integers.
        - Convert the product back to a string and return it.
        Time Complexity: O(n + m) where n and m are the lengths of num1 and num2.
        Space Complexity: O(1) as we are using only a constant amount of extra space.
        """
        def getNumFromString(num):
            n = 0
            for x in num:
                n = n*10 + (ord(x) - ord('0'))
            return n
        return str(getNumFromString(num1) * getNumFromString(num2))
        