class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        s = []
        for i, t in enumerate(temperatures):
            while s and t > s[-1][0]:
                st, si = s.pop()
                res[si] = i - si
            s.append((t, i))
        return res
