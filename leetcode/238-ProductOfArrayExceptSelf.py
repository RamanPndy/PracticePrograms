class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        Steps:
        1. create res array with then same length as nums with prefilled value as 1
        2. create a neutral val as suffix
        3. traverse nums array by index from index 1 and update res at index i by muliplying prev val with prev num
        4. traverse nums array in reverse 
            - update res at index i by muliplying current index val with suffix
            - update suffix by muliplying current nums index val with suffix
        5. return res

        Question: Can you solve this problem without using division and in O(n) time complexity?
        Approach:
        - Use a two-pass approach to calculate the product of all elements except self.
        - In the first pass, calculate the prefix product for each element.
        - In the second pass, calculate the suffix product and multiply it with the prefix product stored in the result array.
        - This approach ensures that we calculate the product of all elements except self without using division and in O(n) time complexity.
        Time Complexity: O(n)
        Space Complexity: O(1) (excluding the output array)
        Example:
        - Input: nums = [1,2,3,4]
        - Output: [24,12,8,6]
        Explanation:
        - For the input [1,2,3,4], the product of all elements except self for each index is calculated as follows:
          - Index 0: 2*3*4 = 24
          - Index 1: 1*3*4 = 12
          - Index 2: 1*2*4 = 8
          - Index 3: 1*2*3 = 6
        """
        res = [1] * len(nums)
        suffix = 1
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res