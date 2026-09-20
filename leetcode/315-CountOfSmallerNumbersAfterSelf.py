class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].
        Input: nums = [5,2,6,1]
        Output: [2,1,1,0]
        Explanation:
        To the right of 5 there are 2 smaller elements (2 and 1).
        To the right of 2 there is only 1 smaller element (1).
        To the right of 6 there is 1 smaller element (1).
        To the right of 1 there is 0 smaller element.

        Steps:
        1. Create a list of pairs where each pair contains the number and its original index.
        2. Use a modified merge sort to sort the pairs.
        3. During the merge process, count the number of smaller elements to the right for each element.
        4. Update the count_map with the counts.
        5. Return the count_map as the result.
        """
        # res = []
        # totalNums = len(nums)
        # for i in range (totalNums):
        #     gt = 0
        #     st = i + 1
        #     for j in range(st, totalNums):
        #         print (nums[i], nums[j], gt)
        #         if nums[i] > nums[j]:
        #             gt += 1
        #     res.append(gt)
        # return res
        n = len(nums)
        self.count_map = [0] * n
        pairs = [(nums[i], i) for i in range(n)]
        self.merge_sort(pairs)
        return self.count_map

    def merge_sort(self, pairs):
        if len(pairs) <=1 :
            return pairs

        mid = len(pairs) // 2
        left = self.merge_sort(pairs[:mid])
        right = self.merge_sort(pairs[mid:])

        self.count_smaller(left, right)
        return self.merge(left, right)

    def count_smaller(self, left, right):
        j = 0
        for i in range (len(left)):
            while j < len(right) and left[i][0] >right[j][0]:
                j +=1 
            original_index = left[i][1]
            self.count_map[original_index] += j

    def merge(self, left, right):
        merged = []
        i = j =0
        while i<len(left) and j <len(right):
            if left[i][0] <= right[j][0]:
                merged.append(left[i])
                i +=1
            else:
                merged.append(right[j])
                j +=1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged