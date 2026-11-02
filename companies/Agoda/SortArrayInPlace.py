'''
Question— Sort an array containing 1, 2 and 3 in place
Problem: Given an array containing only 1, 2, and 3, sort it in ascending order without using a built-in sorting function.

Example:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]

Input:  [2, 1, 3, 2, 1, 3]
Output: [1, 1, 2, 2, 3, 3]

Approach: Use three pointers to divide the array into regions containing 1s, 2s, and 3s.
1. Initialize three pointers: low, mid, and high.
2. Traverse the array with the mid pointer.
3. If the element at mid is 1, swap it with the element at low and increment both low and mid.
4. If the element at mid is 2, just increment mid.
5. If the element at mid is 3, swap it with the element at high and decrement high.
6. Continue until mid exceeds high.

Why this works ?
The algorithm works by maintaining three regions in the array:
1. Elements before the 'low' pointer are all 1s.
2. Elements between 'low' and 'mid' are all 2s.
3. Elements after the 'high' pointer are all 3s.
By swapping elements into their correct regions as we traverse the array, 
we ensure that all 1s, 2s, and 3s are grouped together in ascending order.

Time Complexity: O(n), where n is the length of the array.
Space Complexity: O(1) (in-place sorting)
'''

def sort_array_in_place(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 1:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 2:
            mid += 1
        else:  # arr[mid] == 3
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Example usage:
arr = [3, 3, 2, 1, 3, 2, 1]
sorted_arr = sort_array_in_place(arr)
print(sorted_arr)  # Output: [1, 1, 2, 2, 3, 3, 3]

arr = [2, 1, 3, 2, 1, 3]
sorted_arr = sort_array_in_place(arr)
print(sorted_arr)  # Output: [1, 1, 2, 2, 3, 3]

'''
Likely follow-up: What if the array contains arbitrary integers? 
This particular three-pointer algorithm relies on having exactly three categories. 
For arbitrary integers, use an appropriate general sorting algorithm.
'''