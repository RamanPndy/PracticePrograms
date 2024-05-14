class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        Input: prices = [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

        Steps:
        1. create left and right pointer with value 0 and 1 respectively.
        2. variable maxP will hold maximum profit value
        3. traverse using right point with lenth of prices:
            - if price[left] < price[right]
                - update profit by max of maxP and (prices[right] - prices[left])
            - otherwise left pointer will become right pointer
            - increase right pointer
        4. return maxP
        """
        l , r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP