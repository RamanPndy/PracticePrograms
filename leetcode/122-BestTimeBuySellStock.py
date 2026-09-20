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

        Question: Find the maximum profit from an unlimited number of buy and sell transactions in a list of stock prices.
        Approach:
        - Iterate through the list of prices.
        - Whenever the price of the current day is higher than the previous day, add the difference to the total profit.
        - This simulates buying at the previous day's price and selling at the current day's price.
        - Continue this process for all days to maximize profit.
        Example:

        Input: prices = [7,1,5,3,6,4]
        Output: 7
        Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
        Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
        Total profit is 4 + 3 = 7.
        Another Example:

        Input: prices = [1,2,3,4,5]
        Output: 4
        Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
        Another Example:

        Input: prices = [7,6,4,3,1]
        Output: 0
        Explanation: No transaction is done, i.e., max profit = 0.
        Steps:
        1. Initialize max profit to 0 and start with the price on the first day.
        2. Iterate through the list of prices.
        3. If the current price is higher than the start price, add the difference to max profit.
        4. Update the start price to the current price.
        5. Return the max profit after iterating through all days.
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
