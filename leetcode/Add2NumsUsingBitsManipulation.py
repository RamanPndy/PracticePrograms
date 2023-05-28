class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        if you add 1+1 together, it will roll that over to the next digit, and the value will be 0 at this digit.
        Use ^ operation between a and b to find the different bit
        """
        carry = 0
        mask = 0xffffffff
        while b & mask != 0:
            carry = (a & b) << 1 #this is for handling carry
            a = a ^ b
            b = carry
        return a & mask if b > mask else a