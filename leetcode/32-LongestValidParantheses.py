'''
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.

Example:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Approach:
- Use a stack to keep track of the indices of the characters.
- Initialize the stack with -1 to handle the edge case for the first valid substring.
- Iterate through the string:
    - If the character is '(', push its index onto the stack.
    - If the character is ')', pop the top of the stack.
        - If the stack is empty, push the current index onto the stack.
        - If the stack is not empty, calculate the length of the current valid substring as the difference 
        between the current index and the top of the stack, and update the maximum length.
Time Complexity: O(n)
Space Complexity: O(n)
'''
def longestValidParentheses(s):
    stack = [-1]
    max_length = 0
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    return max_length

if __name__ == "__main__":
    # Example usage:
    print(longestValidParentheses("(()"))  # Output: 2
    print(longestValidParentheses(")()())"))  # Output: 4