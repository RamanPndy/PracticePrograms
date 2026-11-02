class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        Question: Find the number of bulbs that are on after n rounds.
        Approach: A bulb ends up on if it is toggled an odd number of times. A bulb is toggled in each round where its position is a multiple of the round number. Therefore, a bulb is toggled an odd number of times if and only if its position is a perfect square.
        The number of bulbs that are on is equal to the number of perfect squares less than or equal to n.
        Why this works: Only bulbs at positions that are perfect squares have an odd number of factors, and thus are toggled an odd number of times, ending up on.
        """
        return int(n ** 0.5)
        