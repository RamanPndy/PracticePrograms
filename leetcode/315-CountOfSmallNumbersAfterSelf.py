class Solution:
  '''
  Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].
  Example 1:
  Input: nums = [5,2,6,1]
  Output: [2,1,1,0]
  Explanation:
  To the right of 5 there are 2 smaller elements (2 and 1).
  To the right of 2 there is only 1 smaller element (1).
  To the right of 6 there is 1 smaller element (1).
  To the right of 1 there is 0 smaller element.
  
  Example 2:
  Input: nums = [-1]
  Output: [0]
  
  Example 3:
  Input: nums = [-1,-1]
  Output: [0,0]
  '''
    def countSmaller(self, nums):
        n = len(nums)
        result = [0] * n

        arr = list(enumerate(nums))

        def merge_sort(left, right):
            if right - left <= 1:
                return arr[left:right]

            mid = (left + right) // 2

            left_part = merge_sort(left, mid)
            right_part = merge_sort(mid, right)

            merged = []
            i = j = 0
            right_counter = 0

            while i < len(left_part) and j < len(right_part):

                if left_part[i][1] > right_part[j][1]:
                    right_counter += 1
                    merged.append(right_part[j])
                    j += 1
                else:
                    result[left_part[i][0]] += right_counter
                    merged.append(left_part[i])
                    i += 1

            while i < len(left_part):
                result[left_part[i][0]] += right_counter
                merged.append(left_part[i])
                i += 1

            while j < len(right_part):
                merged.append(right_part[j])
                j += 1

            arr[left:right] = merged
            return merged

        merge_sort(0, n)

        return result
