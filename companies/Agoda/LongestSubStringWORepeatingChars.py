'''
Question — Longest substring without repeating characters
Problem: Find the length of the longest substring containing no repeated characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The longest substring without repeating characters is "abc".

Input: s = "bbbbb"
Output: 1
Explanation: The longest substring without repeating characters is "b".

Approach:
1. Use a sliding window to keep track of the current substring without repeating characters.
2. Use a set to store the characters in the current window.
3. Expand the window by adding characters to the right until a duplicate is found.
4. Shrink the window from the left until the duplicate is removed.
5. Keep track of the maximum length of the window during the process.
6. Return the maximum length found.

Why this works:
The algorithm works by maintaining a dynamic window of unique characters and adjusting its size whenever a duplicate 
is encountered. 
This ensures that we always have a substring without repeating characters and can efficiently find the longest one.

why the left pointer never moves backward ?
The left pointer only moves forward when a duplicate character is found in the current window. 
Since we are removing characters from the set as we move the left pointer, we never need to move it backward. 
This ensures that the window always contains unique characters and the algorithm remains efficient.

Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(min(n, m)), where m is the size of the character set (for storing characters in the set).
'''

def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

# Example usage:
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3

s = "bbbbb"
print(length_of_longest_substring(s))  # Output: 1

s = "pwwkew"
print(length_of_longest_substring(s))  # Output: 3

s = ""
print(length_of_longest_substring(s))  # Output: 0

'''
Likely follow-ups:
- Return the substring itself, not just its length.
Approach:
1. Use a sliding window to keep track of the current substring without repeating characters.
2. Use a set to store the characters in the current window.
3. Expand the window by adding characters to the right until a duplicate is found.
4. Shrink the window from the left until the duplicate is removed.
5. Keep track of the maximum length of the window during the process.
6. Return the starting index of the longest substring found.
'''

def longest_substring_without_repeating_characters(s):
    char_set = set()
    left = 0
    max_length = 0
    start_index = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        if right - left + 1 > max_length:
            max_length = right - left + 1
            start_index = left
    return s[start_index:start_index + max_length]

# Example usage:
s = "abcabcbb"
print(longest_substring_without_repeating_characters(s))  # Output: "abc"

s = "bbbbb"
print(longest_substring_without_repeating_characters(s))  # Output: "b"

s = "pwwkew"
print(longest_substring_without_repeating_characters(s))  # Output: "wke"

s = ""
print(longest_substring_without_repeating_characters(s))  # Output: ""

'''
- Return the starting index of the longest substring.
Approach:
1. Use a sliding window to keep track of the current substring without repeating characters.
2. Use a set to store the characters in the current window.
3. Expand the window by adding characters to the right until a duplicate is found.
4. Shrink the window from the left until the duplicate is removed.
5. Keep track of the maximum length of the window during the process.
6. Return the starting index of the longest substring found.
'''

def starting_index_of_longest_substring_without_repeating_characters(s):
    char_set = set()
    left = 0
    max_length = 0
    start_index = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        if right - left + 1 > max_length:
            max_length = right - left + 1
            start_index = left
    return start_index

# Example usage:
s = "abcabcbb"
print(starting_index_of_longest_substring_without_repeating_characters(s))  # Output: 0

s = "bbbbb"
print(starting_index_of_longest_substring_without_repeating_characters(s))  # Output: 0

s = "pwwkew"
print(starting_index_of_longest_substring_without_repeating_characters(s))  # Output: 2

s = ""
print(starting_index_of_longest_substring_without_repeating_characters(s))  # Output: 0