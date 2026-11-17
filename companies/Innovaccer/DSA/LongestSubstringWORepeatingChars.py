'''
Find the longest substring without repeating characters in a given string using sliding window technique.
Use two pointers (start and end) to represent the current window in the string.
Maintain a hash map or array to store the last index of each character.
Expand the end pointer and update the window size if no repetition occurs.
If a repeated character is found, move the start pointer to the right of the previous occurrence.
Keep track of the maximum window size during the iteration.
Example: For input 'abcabcbb', the longest substring without repeating characters is 'abc' with length 3.

Algorithm:
1. Initialize a hash map to store the last index of each character.
2. Initialize start and max_length to 0.
3. Iterate through the string with end pointer.
4. If the character at end is in the hash map and its last index is greater than or equal to start, update start to last index + 1.
5. Update the hash map with the current index of the character.
6. Update max_length with the maximum of max_length and (end - start + 1).
7. Return max_length.

Time Complexity:
- O(n), where n is the length of the string, as each character is processed at most twice.
Space Complexity:
- O(min(n, m)), where m is the size of the character set (e.g., 26 for lowercase English letters), for storing the last index of characters.
'''

def longest_substring_wo_repeating_chars(s):
    last_index = {}
    start = 0
    max_length = 0
    for end, char in enumerate(s):
        if char in last_index and last_index[char] >= start: # If the character is repeated within the current window, move start to the right of its last occurrence
            start = last_index[char] + 1
        last_index[char] = end
        max_length = max(max_length, end - start + 1)
    return max_length

# Example usage:
s = "abcabcbb"
print(longest_substring_wo_repeating_chars(s))  # Output: 3

s = "bbbbb"
print(longest_substring_wo_repeating_chars(s))  # Output: 1

s = "pwwkew"
print(longest_substring_wo_repeating_chars(s))  # Output: 3