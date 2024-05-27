class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        Given an array of integers temperatures represents the daily temperatures, return an array answer such that 
        answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
        If there is no future day for which this is possible, keep answer[i] == 0 instead.
        :type temperatures: List[int]
        :rtype: List[int]
        Input: temperatures = [73,74,75,71,69,72,76,73]
        Output: [1,1,4,2,1,1,0,0]
        Steps:
            1. create result array of temperatures length
            2. create stack
            3. traverse temperatures by index:
                - while stack is not empty and temperature at current index is > stack last element temperature
                    - get stack last element temperature and corresponding index
                    - update result array at stack corresponding index difference of current index and stack last element index.
                - else append (current temperature and it's corresponding index) in stack
            4. retrun result
        """
        res = [0] * len(temperatures)
        s = []
        for i, t in enumerate(temperatures):
            while s and t > s[-1][0]:
                st, si = s.pop()
                res[si] = i - si
            s.append((t, i))
        return res
