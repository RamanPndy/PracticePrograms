'''
Question — Minimum operations to make array elements equal
Problem: Given an array of integers, determine the minimum number of operations required to make all elements equal. 
In one operation, you can increment or decrement an element by 1.

Example:
Input: nums = [1, 2, 3]
Output: 2

Approach:
1. Find the median of the array.
2. Calculate the sum of absolute differences between each element and the median.
3. Return the sum as the minimum number of operations.

Why this works:
The median minimizes the sum of absolute differences, which ensures the minimum number of operations to make all elements equal.
To minimize the total number of increment/decrement operations, we should make every element equal to the median, not the mean.

why not the mean ?
The mean minimizes the sum of squared differences, not the sum of absolute differences. 
Since each operation changes an element by 1, we are concerned with absolute differences, making the median the optimal choice.
The mean minimizes the sum of squared differences:
\[
\sum (x_i-x)^2
\]

The median minimizes the sum of absolute differences:
\[
\sum |x_i-x|
\]

What if the array has an even number of elements?
In this case, there are two middle elements. Either of them can be chosen as the median, and the result will still 
yield the minimum number of operations. 
The algorithm above chooses the upper middle element when the array length is even.

What if incrementing costs 2 and decrementing costs 1?
In this case, the optimal target value may not be the median. We would need to consider the cost of each operation and 
potentially choose a value that minimizes the total cost, which could be different from the median. 
This becomes a more complex optimization problem and may require a different approach than simply using the median.

Remember this pattern:
- Minimum sum of absolute differences → Median
- Minimum sum of squared differences → Mean
- Need only the median, not a sorted array → Quickselect

Time Complexity: O(n log n), where n is the length of the array (due to sorting to find the median).
Space Complexity: O(1), as no additional space is used apart from variables.
'''

def min_operations_to_equal(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

# Example usage:
nums = [1, 2, 3]
print(min_operations_to_equal(nums))  # Output: 2

'''
Quickselect for finding the median without fully sorting the array
Complexity:
- Expected time: \(O(n)\)
- Worst-case time: \(O(n^2)\)
- Auxiliary space: \(O(1)\), excluding the input array.
'''

import random

def quickselect(nums, k):
    left, right = 0, len(nums) - 1

    while left <= right:
        pivot_index = random.randint(left, right)
        pivot = nums[pivot_index]

        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        store = left

        for i in range(left, right):
            if nums[i] < pivot:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1

        nums[store], nums[right] = nums[right], nums[store]

        if store == k:
            return nums[store]
        elif store < k:
            left = store + 1
        else:
            right = store - 1

    return nums[k]


def min_operations_optimized(nums):
    if not nums:
        return 0

    median = quickselect(nums, len(nums) // 2)

    return sum(abs(x - median) for x in nums)


print(min_operations_optimized([1, 2, 3]))       # 2
print(min_operations_optimized([1, 10, 2, 9]))   # 16