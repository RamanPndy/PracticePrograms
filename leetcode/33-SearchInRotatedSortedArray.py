class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4   
        Steps:
        1. create left and right such that left = 0 and right = len(nums) -1
        2. loop while left <= right:
            - get the mid index by (left + right) / 2
            - if mid is the target then return index of mid
            - if mid is >= left number ie. array is left rotated
                if target is in middle of left number and mid ie. nums[left] <= target < nums[mid]
                    decrease right by mid index - 1
                else 
                    increase left by mid index + 1
            - else array is right rotated
                if target is in middle of mid and right number ie. nums[mid] < target <= nums[right]
                    increase left by mid index + 1
                else
                    decrease right by mid index - 1
        3. otherwise return -1
        TC: O(logn)
        """
        l , r = 0, len(nums) -1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                #left rotated
                # 3 4 5 6 7 1 2
                #      mid
                #nums[left] <= target < nums[mid]
                if nums[l] <= target and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                #right rotated
                # 6 7 1 2 3 4 5
                #     mid    
                # nums[mid] < target <= nums[right]
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1