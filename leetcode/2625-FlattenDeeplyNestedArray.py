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
