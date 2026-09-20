class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        if you add 1+1 together, it will roll that over to the next digit, and the value will be 0 at this digit.
        Use ^ operation between a and b to find the different bit

        Question: How can we add two numbers without using the + or - operators?
        Intuition:
        - We can use bitwise operations to simulate the addition process.
        - The XOR (^) operation can be used to add two bits without considering the carry.
        - The AND (&) operation followed by a left shift (<< 1) can be used to calculate the carry.
        - We repeat this process until there is no carry left.

        Approach:
        - Initialize a carry variable to 0.
        - Use a mask to handle overflow for 32-bit integers.
        - While there is a carry:
            - Calculate the carry using (a & b) << 1.
            - Update a using a ^ b.
            - Update b with the carry.
        - Return the result considering the mask for 32-bit overflow.
        
        Time Complexity: O(1) since the number of iterations is limited by the number of bits in the integer.
        Space Complexity: O(1) as we are using a constant amount of extra space.
        """
        carry = 0
        mask = 0xffffffff
        while b & mask != 0:
            carry = (a & b) << 1 #this is for handling carry
            a = a ^ b
            b = carry
        return a & mask if b > mask else a