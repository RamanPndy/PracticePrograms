class Solution(object):
    def nextPermutation(self, nums):
        """
        A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
        For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
        The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

        For example, the next permutation of arr = [1,2,3] is [1,3,2].
        Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
        While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
        Given an array of integers nums, find the next permutation of nums.

        The replacement must be in place and use only constant extra memory.
        Input: nums = [1,2,3]
        Output: [1,3,2] 
        Question: Given an array of integers nums, find the next lexicographically greater permutation of nums in-place.
        Approach:
        - Start from the end of the array and find the first non-increasing element.
        - If the entire array is non-increasing, reverse it to get the smallest permutation.
        - Otherwise, find the first element from the end that is greater than the identified element.
        - Swap these two elements.
        - Reverse the sequence from the position of the first identified element to the end to get the next permutation.
        Time Complexity: O(n) where n is the length of the array.
        Space Complexity: O(1) as we are modifying the array in place.
        Steps:
        1. To find next permutations, we'll start from the end. create 2 vars which have lenght of nums - 1
            # First we'll find the first non-increasing element starting from the end
            After completion of the first loop, there will be two cases
        case 1:
            Our i becomes zero (This will happen if the given array is sorted decreasingly). 
            In this case, we'll simply reverse the sequence and will return 
        case 2:
        3. If it's not zero then we'll find the first number grater then nums[i-1] starting from end
            # Now our pointer is pointing at two different positions
            # i. first non-ascending number from end
            # j. first number greater than nums[i-1]
            # We'll swap these two numbers
            # We'll reverse a sequence strating from i to end
        """
        i = j = len(nums) -1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return
        
        while nums[j] <= nums[i-1]:
            j -= 1

        # Swap the numbers at positions i-1 and j, then reverse the sequence from i to the end.
        nums[i-1], nums[j] = nums[j], nums[i-1]
        # Reverse the sequence from i to the end to get the next permutation.
        nums[i:] = nums[len(nums)-1:i-1:-1]