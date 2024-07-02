class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Input: nums = [5,7,7,8,8,10], target = 8
        Output: [3,4]

        Input: nums = [5,7,7,8,8,10], target = 6
        Output: [-1,-1]

        Steps:
        1. Find the Index of the Smallest Element: 
            This index will help in determining the rotation point. 
            Use a modified binary search to find this index.
            Find Rotation Index:
            function which will identify the smallest element's index, which indicates the rotation 
            point of the array.
        2. Binary Search in the Two Halves:
            Depending on the rotation point, determine which part of the array to perform the 
            binary search on for the target element.
            to determine if the target is in the first half or the second half of the rotated array.
        3. Find the First and Last Position:
            Use binary search again to find the first and last occurrences of the target.
            locate the first and last occurrences of the target using binary search principles.
        TC: O(logn)
        """
        n = len(nums)
        if n == 0:
            return [-1, -1]
        rotation_index = self.find_rotation_index(nums)
        # If the target is the smallest element
        # if nums[rotation_index] == target:
        #     return [rotation_index, rotation_index]
        
        # Determine which part of the array to search
        if rotation_index == 0 or target < nums[0]:
            start = self.binary_search(nums, rotation_index, n - 1, target)
        else:
            start = self.binary_search(nums, 0, rotation_index - 1, target)

        if start == -1:
            return [-1, -1]

        first_position = self.find_first_position(nums, 0, n - 1, target)
        last_position = self.find_last_position(nums, 0, n - 1, target)

        return [first_position, last_position]

    # Helper function to find the index of the smallest element (rotation point)
    def find_rotation_index(self,nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left
    
    # Helper function to perform binary search
    def binary_search(self,nums, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    # Function to find the first position of the target
    def find_first_position(self, nums, left, right, target):
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return index

    # Function to find the last position of the target
    def find_last_position(self,nums, left, right, target):
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return index