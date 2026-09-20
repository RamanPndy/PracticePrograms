class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
        You are given two integer array position and speed, both of length n, where position[i] is the starting mile of the 
        ith car and speed[i] is the speed of the ith car in miles per hour.
        A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
        A car fleet is a car or cars driving next to each other. 
        The speed of the car fleet is the minimum speed of any car in the fleet.
        If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
        Return the number of car fleets that will arrive at the destination.

        Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
        Output: 3
        Explanation:
        The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
        The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
        The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
        
        Question: How many car fleets will arrive at the destination?
        Intuition: Cars that are closer to the target and have slower speeds will form fleets with cars behind them if those cars catch up.
        Steps:
        1. Pair each car's position with its speed.
        2. Sort the cars by their starting position in descending order.
        3. Calculate the time each car will take to reach the target.
        4. Use a stack to keep track of the fleets based on their arrival times.
        5. Iterate through the times and count the number of fleets.
        Time Complexity: O(n log n), where n is the number of cars, due to sorting the cars by their starting position.
        Space Complexity: O(n) for the stack used to keep track of the fleets.
        Interview Explanation: The key insight is to recognize that cars closer to the target with slower speeds will form fleets with cars behind them if those cars catch up. By calculating the time each car takes to reach the target and using a stack to track the fleets, we can determine the number of car fleets that will arrive at the destination.
        """
        stack = []
        ps = [(p,s) for p,s in zip(position,speed)]
        ps.sort(key=lambda x: (x[0], x[1]), reverse=True)
        # print(ps)
        for p,s in ps:
            t = float(target-p)/s
            stack.append(t)
        print (stack)
        res = cur = 0
        for t in stack :
            if t > cur :
                res = res + 1
                cur = t
        return res
            