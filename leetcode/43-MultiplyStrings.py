class Solution(object):
    def multiply(self, num1, num2):
        """
        Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

        Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
        Input: num1 = "2", num2 = "3"
        Output: "6"
        """
        def getNumFromString(num):
            n = 0
            for x in num:
                n = n*10 + (ord(x) - ord('0'))
            return n
        return str(getNumFromString(num1) * getNumFromString(num2))
        