class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        Input: coins = [1,2,5], amount = 11
        Output: 3
        Explanation: 11 = 5 + 5 + 1
        If we imagine the search as a tree, what is " the fewest number of coins that you need to make up that amount" 
        It is the shortest path! And the shortest path is BFS. So, when you use BFS you don't have to think about the minimum: the first found number of coins will be the answer.
        Steps:
        1. create a queue and append (amount and num of coins(to be calculated)) along with visited set
        2. traverse queue and get current amount and num of coins
        3. if current amount is 0 then return num of coins
        4. traverse each coin
            - get new amount by subtracting coin from current amount
            - if new amount already present in visited or new amount is negative then continue
            - increase num of coins and append (new amount and increased num of coins) in queue
            - add new amount in visited
        """
        q = [(amount, 0)]
        visited = set()
        while q:
            currAmt, numCoins = q.pop(0)
            if currAmt == 0:
                return numCoins
            for c in coins:
                newamt = currAmt - c

                if newamt in visited or newamt < 0:
                    continue
                
                q.append((newamt, numCoins + 1))
                visited.add(newamt)
        return -1
        # dp = [amount + 1] * (amount +1)
        # dp[0] = 0
        # for a in range(1,amount+1):
        #     for c in coins:
        #         if a-c >= 0:
        #             dp[a] = min(dp[a], 1 + dp[a-c])
        # return dp[amount] if dp[amount] != amount + 1 else -1