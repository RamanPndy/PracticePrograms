class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        You are playing a video game where you are defending your city from a group of n monsters. 
        You are given a 0-indexed integer array dist of size n, where dist[i] is the initial distance in kilometers of 
        the ith monster from the city.
        The monsters walk toward the city at a constant speed. 
        The speed of each monster is given to you in an integer array speed of size n, 
        where speed[i] is the speed of the ith monster in kilometers per minute.
        You have a weapon that, once fully charged, can eliminate a single monster. 
        However, the weapon takes one minute to charge. The weapon is fully charged at the very start.
        You lose when any monster reaches your city. If a monster reaches the city at the exact moment the weapon is 
        fully charged, it counts as a loss, and the game ends before you can use your weapon.
        Return the maximum number of monsters that you can eliminate before you lose, or n if you can eliminate all 
        the monsters before they reach the city.

        Example 1:
        Input: dist = [1,3,4], speed = [1,1,1]
        Output: 3
        Explanation:
        In the beginning, the distances of the monsters are [1,3,4]. You eliminate the first monster.
        After a minute, the distances of the monsters are [X,2,3]. You eliminate the second monster.
        After a minute, the distances of the monsters are [X,X,2]. You eliminate the third monster.
        All 3 monsters can be eliminated.

        Example 2:
        Input: dist = [1,1,2,3], speed = [1,1,1,1]
        Output: 1
        Explanation:
        In the beginning, the distances of the monsters are [1,1,2,3]. You eliminate the first monster.
        After a minute, the distances of the monsters are [X,0,1,2], so you lose.
        You can only eliminate 1 monster.

        Example 3:
        Input: dist = [3,2,4], speed = [5,3,2]
        Output: 1
        Explanation:
        In the beginning, the distances of the monsters are [3,2,4]. You eliminate the first monster.
        After a minute, the distances of the monsters are [X,0,2], so you lose.
        You can only eliminate 1 monster.

        Approach:
        1. Calculate the arrival time for each monster as (dist[i] + speed[i] - 1) // speed[i].
        2. Sort the arrival times in ascending order.
        3. Iterate through the sorted arrival times, eliminating one monster per minute.
        4. If the current time is greater than or equal to the monster's arrival time, stop and return 
        the count of eliminated monsters.
        5. If all monsters are eliminated before any reach the city, return n.

        Why this works:
        By sorting the monsters based on their arrival times, we ensure that we always deal with the most urgent threat 
        first. 
        Eliminating one monster per minute in this order maximizes the number of monsters we can eliminate before any 
        reach the city.

        Time complexity:
        O(n log n) due to sorting the times array.

        Space complexity:
        O(n) for storing the times array.
        """
        arrival_times = []

        for d, s in zip(dist, speed):
            arrival_time = (d + s - 1) // s
            arrival_times.append(arrival_time)

        arrival_times.sort()

        for i, arrival_time in enumerate(arrival_times):
            if arrival_time <= i:
                return i

        return len(dist)