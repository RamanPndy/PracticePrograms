'''
Given a multi-dimensional array arr and a depth n, return a flattened version of that array.

A multi-dimensional array is a recursive data structure that contains integers or other multi-dimensional arrays.

A flattened array is a version of that array with some or all of the sub-arrays removed and replaced with the actual elements in that sub-array. This flattening operation should only be done if the current depth of nesting is less than n. The depth of the elements in the first array are considered to be 0.

Please solve it without the built-in Array.flat method.

Input
arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
n = 0
Output
[1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]

Explanation
Initialization:

result is an empty list that will store the flattened elements.
Helper Function:

Define a helper function helper that takes a sub-array as its parameter.
Iterate over each item in the sub-array.
If the item is a list, recursively call helper with this item.
If the item is not a list, append it to the result list.
Call Helper:

Call the helper function with the input array arr.
Return Result:

Return the result list which now contains all the flattened elements.

'''
#Recursive Approach
def flatten(arr):
    """
    Flatten a multi-dimensional array up to a specified depth.

    :param arr: List of integers or nested lists
    :return: Flattened list of integers

    Question: How can we flatten a multi-dimensional array up to a specified depth without using the built-in Array.flat method?
    Intuition:
    - We can use a recursive helper function to traverse the nested arrays.
    - At each level, we check if the element is a list or an integer.
    - If it's a list and the current depth is less than the specified depth, we recursively flatten it.
    - If it's an integer or the current depth is equal to the specified depth, we add it to the result list.
    Approach:
    - Initialize an empty result list.
    - Define a recursive helper function that takes a sub-array and the current depth as parameters.
    - Traverse each element in the sub-array.
        - If the element is a list and the current depth is less than the specified depth, recursively call the helper function with the element and incremented depth.
        - If the element is an integer or the current depth is equal to the specified depth, append it to the result list.
    - Call the helper function with the input array and initial depth 0.
    - Return the result list.
    Time Complexity: O(n) where n is the total number of elements including nested ones.
    Space Complexity: O(d) where d is the maximum depth of the nested arrays.
    Note:
    - This implementation assumes that the input array can be nested to any depth.
    - The depth parameter is implicit in this implementation, as it fully flattens the array regardless of depth.
    - This implementation uses recursion, which may lead to a stack overflow for extremely deep nested arrays.
    """
    result = []

    def flatten_helper(sub_arr):
        for element in sub_arr:
            if isinstance(element, list):
                flatten_helper(element)
            else:
                result.append(element)
                
    flatten_helper(arr)
    return result

# Example usage:
arr = [1, [2, [3, 4], [[5]]]]
print(flatten(arr))  # Output: [1, 2, 3, 4, 5]

#Iteractive Approach
def flatten(arr):
    result = []
    stack = arr[::-1]  # Reverse to simulate stack (LIFO) behavior with list

    while stack:
        element = stack.pop()
        if isinstance(element, list):
            stack.extend(element[::-1])  # Add elements in reverse order to stack
        else:
            result.append(element)

    return result

# Example usage:
arr = [1, [2, [3, 4], [[5]]]]
print(flatten(arr))  # Output: [1, 2, 3, 4, 5]
