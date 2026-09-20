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
  Steps:
  1. Enumerate the elements of the array to keep track of their original indices.
  2. Use a modified merge sort to count the number of smaller elements to the right.
  3. During the merge step, for each element in the left part, count how many elements in the right part are smaller.
  4. Update the result array with these counts.
  5. Return the result array after the merge sort is complete.
  Intuition: The problem can be solved using a modified merge sort, where during the merge step, we count the number of smaller elements to the right for 
  each element in the left part.
  Time Complexity: O(n log n)
  Space Complexity: O(n)
  Implementation Details: The merge sort is modified to keep track of the original indices of the elements, and during the merge step, 
  the number of smaller elements to the right is counted and updated in the result array.
  Example Walkthrough:
  For nums = [5,2,6,1], the merge sort will proceed as follows:
  1. Split into [5,2] and [6,1]
  2. Split [5,2] into [5] and [2], merge to get [2,5] and update counts: [1,0]
  3. Split [6,1] into [6] and [1], merge to get [1,6] and update counts: [1,0]
  4. Merge [2,5] and [1,6] to get [1,2,5,6] and update counts: [2,1,1,0]
  The walkthrough demonstrates how the merge sort helps in counting the smaller elements to the right for each element in the array.
  This approach ensures that we efficiently count the smaller elements to the right for each element in the array while maintaining the overall time complexity of O(n log n).
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
