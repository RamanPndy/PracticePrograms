from collections import defaultdict

class Solution:
    '''
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and using only constant extra space.
    Input: nums = [1,3,4,2,2]
    Output: 2

    '''

    def findDuplicate(self, nums) -> int:
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
        for k,v in m.items():
            if v > 1:
                return k
            
    def findDuplicate(self, nums) -> int:
        #using Floyd's Tortoise and Hare algorithm
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow