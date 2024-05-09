class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        Input: nums = [1,2,3]
        Output: [1,3,2] 
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
        
        nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:] = nums[len(nums)-1:i-1:-1]