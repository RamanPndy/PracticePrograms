class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Input: nums = [100,4,200,1,3,2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
        Steps:
        1. create a set of unique nums and set longest_seq to 0
        2. traverse nums
            a. If the element is the start of the sequence (i.e., the element-1 is not present in the hash set), 
            do the following:
            i. Initialize variables to store the length of the current sequence to 1 also to hold current number.
            ii. Keep incrementing the current number by 1 and checking if the next number is present in the hash set.
            iii. If the next number is present in the hash set, increment the length of the current sequence and current number by 1
            iv. If the length of the current sequence is greater than the length of the longest sequence found so far, 
            update the length of the longest sequence found so far.
        """
        numSet = set(nums)
        longest_seq = 0
        for n in nums:
            if n-1 not in numSet:
                curr_num = n
                cur_seq = 1
                while curr_num + 1 in numSet:
                    curr_num += 1
                    cur_seq += 1
                longest_seq = max(cur_seq, longest_seq)
        return longest_seq