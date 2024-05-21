class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
        You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next 
        (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
        Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit 
        once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.
        Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        Output: 3
        Explanation:
        Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
        Travel to station 4. Your tank = 4 - 1 + 5 = 8
        Travel to station 0. Your tank = 8 - 2 + 1 = 7
        Travel to station 1. Your tank = 7 - 3 + 2 = 6
        Travel to station 2. Your tank = 6 - 4 + 3 = 5
        Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
        Therefore, return 3 as the starting index.
        Steps:
        1. create vars for balance, deficit and start and set to 0.
        2. traverse through length of gas stations by index
            - calculate balance by subtracting gas with cost at current index
            - if balance is negative i.e. we can not choose current index and we need to opt of next index
                - start becomes next index
                - update deficit by adding negative balance
                - reset balance to 0
        3. if sum of balance and deficit is postive then return start index.
        4. otherwise return -1.
        """
        balance = deficit = start = 0
        for i in range(len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                deficit += balance
                start = i +1
                balance = 0
        if balance + deficit >= 0:
            return start
        return -1