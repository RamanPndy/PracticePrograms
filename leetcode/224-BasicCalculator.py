'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
'''
def calculate(s: str) -> int:
    '''
    Initialization:
        stack is used to store numbers and operators.
        num is used to keep track of the current number being processed.
        op is the current operator (+ by default).
        i is the index for iterating through the string.
    Main Loop:
        Digit Characters: If the character is a digit, build the number (num).
        Operators or End of String: If the character is an operator (+, -, or (), or the end of the string is reached:
            Call update to push the current number with its operator onto the stack.
            Reset num to 0 and set op to the current operator.
        Closing Parenthesis ): If a closing parenthesis is encountered:
            Pop numbers from the stack and sum them until an operator is found.
            Pop the operator and update the stack with the resulting number.
    Sum of Stack: Finally, sum up the stack which contains all the numbers to get the result.
    Question: Implement a basic calculator to evaluate a valid mathematical expression represented as a string.
    Approach:
        - Use a stack to keep track of numbers and operators.
        - Iterate through the string character by character.
        - Build numbers from consecutive digits.
        - When encountering an operator or parenthesis, update the stack accordingly.
        - Handle closing parentheses by summing up the numbers until the corresponding opening parenthesis is found.
        - Finally, sum up the stack to get the result.
        Time: O(n) where n is the length of the string, as we iterate through the string once.
        Space: O(n) for the stack used to store numbers and operators.
    '''
    def update(op, val):
        if op == '+':
            stack.append(val)
        if op == '-':
            stack.append(-val)

    stack = []
    num, op = 0, "+"
    i = 0

    while i < len(s):
        char = s[i]

        if char.isdigit():
            num = num * 10 + int(char)

        if char in "+-(" or i == len(s) - 1:
            update(op, num)
            num, op = 0, char

        if char == ")":
            num = 0
            while isinstance(stack[-1], int):
                num += stack.pop()
            op = stack.pop()
            update(op, num)
            num = 0

        i += 1

    return sum(stack)

# Example usage:
s = "(1+(4+5+2)-3)+(6+8)"
print(calculate(s))  # Output: 23
