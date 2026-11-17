'''
Sort a rotated sorted array by identifying the rotation point and rearranging elements to restore sorted order.

- A rotated sorted array is a sorted array rotated at some pivot unknown to you beforehand, e.g., [4,5,6,7,0,1,2].
- To sort it, find the pivot (smallest element) using binary search in O(log n) time.
- Once pivot is found, split the array into two sorted subarrays and merge them to get the fully sorted array.
- Example: Input: [4,5,6,7,0,1,2], pivot at index 4 (value 0), sorted array: [0,1,2,4,5,6,7].

Algorithm:
1. Use binary search to find the index of the smallest element (pivot).
2. Split the array into two subarrays at the pivot.
3. Merge the two sorted subarrays to get the fully sorted array.

Time Complexity:
- Finding the pivot using binary search: O(log n)
- Merging the two sorted subarrays: O(n)
Overall: O(n)
Space Complexity:
- O(n) for the merged array
'''
def sort_rotated_array(arr):
    if not arr:
        return []

    # Find the pivot (index of the smallest element)
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[high]: # Mid element is greater than the last element, pivot must be in the right half
            low = mid + 1 # Pivot must be in the right half
        else: # Mid element is less than or equal to the last element, pivot is in the left half or at mid
            high = mid # Pivot must be in the left half or at mid
    pivot = low # Index of the smallest element (rotation point)

    # Merge the two sorted subarrays
    return arr[pivot:] + arr[:pivot]

# Example usage:
arr = [4,5,6,7,0,1,2]
sorted_arr = sort_rotated_array(arr)
print(sorted_arr)  # Output: [0,1,2,4,5,6,7]