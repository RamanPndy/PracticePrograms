class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4   
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