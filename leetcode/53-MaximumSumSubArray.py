class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Given an integer array nums, find the subarray with the largest sum, and return its sum.
        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: The subarray [4,-1,2,1] has the largest sum 6.

        Question: Can you solve this problem in O(n) time complexity and O(1) space complexity?
        Approach:
        - Use a greedy approach to keep track of the maximum subarray sum ending at the current index.
        - Maintain a variable to store the maximum sum found so far.
        - Iterate through the array, updating the current maximum subarray sum and the overall maximum sum.
        - If the current maximum subarray sum becomes negative, reset it to 0.
        - Return the overall maximum sum at the end.
        Time complexity: O(n), where n is the number of elements in the array.
        Space complexity: O(1), as we are using only a constant amount of extra space.
        Notes:
        - This problem is commonly known as the "Maximum Subarray" problem or "Kadane's Algorithm".
        - The key idea is to keep track of the maximum sum ending at the current index and reset it when it becomes negative.
        - Kadane's Algorithm efficiently finds the maximum subarray sum in a single pass through the array.
        - The algorithm works by iterating through the array and maintaining the maximum subarray sum ending at the current index.
        - This approach ensures that we only traverse the array once, making it highly efficient.
        Steps:
        1. create answer variable and assing positive infinity as max value
        2. create variable maximum and set it to 0.
        3. travers numbers
            - add number to maximum
            - update answer by max of answer and maximum value so far
            - update maximum by max of maximum and 0
        4. return answer
        """
        answer = float('-inf')
        maximum=0

        for num in nums:
            maximum += num
            answer = max(answer, maximum)
            maximum = max(maximum, 0)
        return answer 