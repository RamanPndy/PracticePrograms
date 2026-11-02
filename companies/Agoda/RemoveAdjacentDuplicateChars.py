'''
Question — Remove adjacent duplicate characters
Problem: Repeatedly remove adjacent equal characters until no adjacent duplicates remain.

Example:
Input: "abbaca"
Output: "ca"

Explanation:
Step 1: "abbaca" → "aaca" (remove "bb")
Step 2: "aaca" → "ca" (remove "aa")

Approach:
Use a stack to keep track of characters. Iterate through the string, and for each character:
1. If the stack is not empty and the top of the stack is equal to the current character, 
pop the stack (remove the duplicate).
2. Otherwise, push the current character onto the stack.
3. After processing all characters, the stack will contain the result without adjacent duplicates.
4. Convert the stack back to a string and return it.

Why this works:
The algorithm works by using a stack to keep track of characters. Whenever a duplicate is found,
it is removed immediately by popping the stack. 
This ensures that all adjacent duplicates are removed in a single pass through the string, 
and the final stack contains the result without any adjacent duplicates.

Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(n), for the stack used to store characters.
'''
def remove_adjacent_duplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char: # If the current character is the same as the top of the stack, it's a duplicate, so pop it.
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

# Example usage:
s = "abbaca"
print(remove_adjacent_duplicates(s))  # Output: "ca"

s = "azxxzy"
print(remove_adjacent_duplicates(s))  # Output: "ay"

'''
Likely follow-up: 
- Remove groups of k adjacent identical characters. Store (character, count) pairs on the stack and remove a group 
when its count reaches k.
Approach:
1. Initialize an empty stack to store (character, count) pairs.
2. Iterate through the string, and for each character:
   a. If the stack is not empty and the top character is the same as the current character, increment the count.
   b. If the count reaches k, pop the stack (remove the group).
   c. If the stack is empty or the top character is different, push (character, 1) onto the stack.
3. After processing all characters, construct the result string by repeating each character by its count in the stack.
4. Return the result string.
'''

def remove_adjacent_duplicates_k(s, k):
    stack = []
    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([char, 1])
    result = ''.join(char * count for char, count in stack)
    return result

# Example usage:
s = "deeedbbcccbdaa"
k = 3
print(remove_adjacent_duplicates_k(s, k))  # Output: "aa"