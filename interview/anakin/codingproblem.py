# Question: Write a function that takes a mathematical expression as a string input and evaluates it. The expression can contain parentheses, positive integers, and the four basic arithmetic operators (+, -, *, /). However, the expression may also include unary minus (-) operators for negation. The function should return the result of the evaluated expression.
# Example Test Cases:
# For the input string "3 + -4 * (2 - 1)", the function should return -1.
# For the input string "-5 * (7 + 2) / -3 - 1", the function should return 14.
# For the input string "(4 + -6) * 2 - (-8 / 4)", the function should return -2.
# Note:
# The input expression will always be well-formed and valid.
# The unary minus can appear before a number or an expression enclosed in parentheses.
# The result will always be an integer.
# Consider the usual precedence rules of the operators: * and / before + and -.

# To evaluate a mathematical expression with parentheses, unary minus, and the four basic arithmetic operators, you can use the following approach:

# Define a helper function calculate(a, operator, b) that takes two numbers a and b, and an operator (+, -, *, or /). This function performs the corresponding arithmetic operation and returns the result.

# Define the main function evaluate_expression(expression) that takes the input string as an argument. This function will use a stack to evaluate the expression.

# Initialize an empty stack.

# Iterate over each character in the expression:

# a. If the character is a digit, continue reading the entire number until a non-digit character is encountered. Convert the string representation of the number to an integer and push it onto the stack.

# b. If the character is an opening parenthesis '(', push it onto the stack.

# c. If the character is a closing parenthesis ')', start popping elements from the stack until an opening parenthesis is encountered. Evaluate each popped element and its corresponding operator, then push the result back onto the stack.

# d. If the character is an operator (+, -, *, or /), push it onto the stack.

# Once the iteration is complete, there should be a single element remaining on the stack, which is the final result of the expression. Pop and return this element.

def calculate(a, operator, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a // b  # Integer division to match the expected result

def evaluate_expression(expression):
    stack = []

    for char in expression:
        if char.isdigit():
            # Read the entire number and convert it to an integer
            num = ''
            while char.isdigit():
                num += char
                char = next(expression)
            stack.append(int(num))
            continue

        if char in '+-*/':
            stack.append(char)

        elif char == '(':
            stack.append(char)

        elif char == ')':
            # Evaluate the expression inside parentheses
            sub_expression = []
            while stack and stack[-1] != '(':
                sub_expression.append(stack.pop())

            stack.pop()  # Discard the opening parenthesis

            # Reverse the sub-expression to maintain correct order
            sub_expression.reverse()

            result = sub_expression[0]
            for i in range(1, len(sub_expression), 2):
                result = calculate(result, sub_expression[i], sub_expression[i + 1])

            stack.append(result)

    # Evaluate the remaining expression on the stack
    while stack:
        b = stack.pop()
        operator = stack.pop()
        a = stack.pop()
        result = calculate(a, operator, b)
        stack.append(result)

    return stack[0]

# Test cases
print(evaluate_expression("3 + -4 * (2 - 1)"))  # Output: -1
print(evaluate_expression("-5 * (7 + 2) / -3 - 1"))  # Output: 14
print(evaluate_expression("(4 + -6) * 2 - (-8 / 4)"))  # Output: -2
