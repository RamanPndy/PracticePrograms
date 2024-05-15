class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Input: nums = [1,2,3,1]
        Output: 2
        Explanation: 3 is a peak element and your function should return the index number 2.

        Input: nums = [1,2,1,3,5,6,4]
        Output: 5
        Explanation: Your function can return either index number 1 where the peak element is 2, or 
        index number 5 where the peak element is 6.

        Steps:
        1. For sorted arrays, peak element will be one of the extremes like first element or last element. 
           For unsorted array, element will fall in between.
           So If we use binary search and check that if mid element is greater than right value then one of three cases 
           will be applicable to subarray that is left to mid
            a) Left subarray is ascending, in which case, mid-1 is less than mid and mid is the answer.
            b) Left subarray is descending, in which case, first element is the answer.
            c) Peak element lies in between 0 and mid.
        2. So, we move r to the mid
            Else if mid is less than right element then we move to right subarray in which above three cases are again applicable.
            l will move to peak value ultimately.
        3. create left and right with values 0 and len(nums) -1 respectively.
        4. traverse while left < right:
            - get the mid index
            - if numbers[mid] < numbers[mid +1]:
                - increase left
            - otherwise right will become mid index
        5. return left
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[m + 1]:
                l = m +1
            else:
                r = m
        return l
        