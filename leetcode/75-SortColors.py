class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        Question:
        Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

        Example:
        Input: nums = [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]

        Approach:
        Use the Dutch National Flag algorithm with three pointers: low, mid, and high.
        1. Initialize low = 0, mid = 0, high = len(nums) - 1.
        2. Iterate while mid <= high:
           - If nums[mid] == 0, swap nums[low] and nums[mid], increment low and mid.
           - If nums[mid] == 1, increment mid.
           - If nums[mid] == 2, swap nums[mid] and nums[high], decrement high.

        Why this works:
        By maintaining three regions (0s, 1s, and 2s) and adjusting pointers accordingly, we can sort the array in a single pass.

        Time complexity:
        O(n) where n is the length of the array.

        Space complexity:
        O(1) as we are using constant extra space.
        """
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        