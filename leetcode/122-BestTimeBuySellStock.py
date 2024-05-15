class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
        However, you can buy it then immediately sell it on the same day.
        Infinite Transactions

        Time : O(n)
        Space: O(1)

        Input: prices = [7,1,5,3,6,4]
        Output: 7
        Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
        Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
        Total profit is 4 + 3 = 7.
        """
        maxP = 0
        # price of stock on first day
        start = prices[0]
        totalNumOfDays = len(prices)
        for i in range(totalNumOfDays):
            if start < prices[i]:
                maxP += prices[i] - start
            start = prices[i]
        return maxP
