class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        Question:
        Reverse the digits of the given 32-bit signed integer x.

        Approach:
        - Extract digits from the end of the number and build the reversed number.
        - Handle the sign of the number separately.
        - Check for overflow and return 0 if the reversed number exceeds the 32-bit signed integer range.

        Complexity Analysis:
        - Time: O(log10(x)) because we process each digit of the number once.
        - Space: O(1) since we use a constant amount of extra space.

        Steps:
        1. Determine the sign of the number and work with its absolute value.
        2. Extract digits from the end of the number and build the reversed number.
        3. Apply the sign to the reversed number.
        4. Check for overflow and return 0 if the reversed number exceeds the 32-bit signed integer range.
        """
        ans = 0
        sign = 1 if x > 0 else -1
        x *= sign
        while x > 0:
            temp = x % 10
            ans = ans * 10 + temp
            x = x // 10
        ans *= sign
        return ans if ans > (-2 ** 31) and ans < (2 ** 31) -1 else 0