def next_greater_element(arr):
    """
    Find the next greater element for each element in the array.

    :param arr: List[int] - input array
    :return: List[int] - array of next greater elements, -1 if no greater element exists

    Question : Given an array arr[] of integers, determine the Next Greater Element (NGE) for every element in the array, maintaining the order of appearance. 
    The Next Greater Element for an element x is defined as the first element to the right of x in the array that is strictly greater than x. 
    If no such element exists for an element, its Next Greater Element is -1. 
    Examples: 
    Input: arr[] = [1, 3, 2, 4] 
    Output: [3, 4, 4, -1] Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since it doesn't exist, it is -1. 
    Input: arr[] = [6, 8, 0, 1, 3] 
    Output: [8, -1, 1, 3, -1] 
    Explanation: The next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1 , for 1 it is 3 and then 
    for 3 there is no larger element on right and hence -1.

    Approach:
    The standard O(n) solution uses a monotonic decreasing stack.
    Use a stack to keep track of elements for which we haven't found the next greater element yet.
    Iterate through the array from right to left, and for each element, pop elements from the stack
    if they are less than or equal to the current element. The top of the stack, if it exists, will be the next greater element.
    Finally, any elements left in the stack do not have a next greater element, so their values remain -1 in the result list.

    Time Complexity: O(n), where n is the number of elements in the array, because each element is pushed and popped from the stack at most once.
    Space Complexity: O(n), for the stack and the result list.

    Steps:
    1. Initialize an empty result list with -1 for each element and an empty stack.
    2. Traverse the array from right to left.
    3. For each element, while the stack is not empty and the top of the stack is less than or equal to the current element, pop the stack.
    4. If the stack is not empty after this, the top of the stack is the next greater element for the current element. Update the result list accordingly.
    5. Push the current element's index onto the stack.
    6. Continue to the next element on the left.
    7. Return the result list after the traversal is complete.
    """
    n = len(arr)
    result = [-1] * n
    stack = []  # stores indices

    for i in range(n - 1, -1, -1):

        # Remove elements that are not greater than arr[i]
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        # Top of stack is the next greater element
        if stack:
            result[i] = arr[stack[-1]]

        # Current element can be the NGE for elements on its left
        stack.append(i)

    return result

def next_greater_element(arr):
    '''
    Find the next greater element for each element in the array.
    
    Args:
    arr (List[int]): The input array.

    Returns:
    List[int]: A list where each element is replaced by the next greater element to its right, or -1 if no such element exists.

    Approach:
    Use a stack to keep track of elements for which we haven't found the next greater element yet.
    Iterate through the array from right to left, and for each element, pop elements from the stack
    if they are less than or equal to the current element. The top of the stack, if it exists, will be the next greater element.
    Finally, any elements left in the stack do not have a next greater element, so their values remain -1 in the result list.

    Time Complexity: O(n), where n is the number of elements in the array, because each element is pushed and popped from the stack at most once.
    Space Complexity: O(n), for the stack and the result list.

    Example:
    Input: [4, 5, 2, 25]
    Output: [5, 25, 25, -1]
    '''
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr) - 1, -1, -1):

        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result