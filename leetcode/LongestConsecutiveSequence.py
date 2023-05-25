class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        a. If the element is the start of the sequence (i.e., the element-1 is not present in the hash set), do the following:
        i. Initialize a variable to store the length of the current sequence to 1.
        ii. Keep incrementing the element by 1 and checking if the next element is present in the hash set.
        iii. If the next element is present in the hash set, increment the length of the current sequence by 1.
        iv. If the length of the current sequence is greater than the length of the longest sequence found so far, update the length of the longest sequence found so far.
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