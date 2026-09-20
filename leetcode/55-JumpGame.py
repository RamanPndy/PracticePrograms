class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        Input: nums = [2,3,1,1,4]
        Output: true
        Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
        Return true if you can reach the last index, or false otherwise.

        Question: Can you reach the last index of the array starting from the first index, given that each element represents the maximum jump length at that position?
        Approach:
        - Initialize a variable `reach` to keep track of the farthest index that can be reached.
        - Iterate through the array with index `i` and value `n`.
        - If the current index `i` is greater than `reach`, return False as it is not possible to reach this index.
        - Update `reach` to be the maximum of its current value and `i + n`.
        - If the loop completes, return True as the last index is reachable.

        Time complexity: O(n), where n is the length of the array.
        Space complexity: O(1), as we are using only a constant amount of extra space.
        Steps:
        1. Initialize a variable `reach` to 0.
        2. Iterate through the array with index `i` and value `n`.
            - If `i` is greater than `reach`, return False.
            - Update `reach` to be the maximum of its current value and `i + n`.
        3. If the loop completes, return True.
        """
        reach = 0
        for i, n in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + n)
        return True