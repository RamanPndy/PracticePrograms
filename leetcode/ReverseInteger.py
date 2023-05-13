class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
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