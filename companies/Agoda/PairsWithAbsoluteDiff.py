'''
Question — Find pairs with a given absolute difference
Problem: Return the unique pairs of values whose absolute difference is k

Example:
Input: nums = [1, 5, 3, 4, 2], k = 2
Output: [(1, 3), (3, 5), (2, 4)]
Explanation: The pairs with absolute difference 2 are (1, 3), (3, 5), and (2, 4).

Approach:
1. Use a set to store the unique numbers from the input list.
2. Iterate through the set and check if the number plus k exists in the set.
3. If it exists, add the pair (number, number + k) to the result list.
4. Return the result list containing unique pairs.

Why this works:
The algorithm works by using a set to efficiently check for the existence of the complement (num + k) for each unique number. 
This ensures that each pair is counted only once and avoids duplicates.

Time Complexity: O(n), where n is the number of unique elements in the input list.
Space Complexity: O(n), for storing the unique elements in a set.
'''

def find_pairs_with_absolute_diff(nums, k):
    unique_nums = set(nums)
    result = []
    for num in unique_nums:
        if num + k in unique_nums:
            result.append((num, num + k))
    return result

# Example usage:
nums = [1, 5, 3, 4, 2]
k = 2
print(find_pairs_with_absolute_diff(nums, k))  # Output: [(1, 3), (3, 5), (2, 4)]