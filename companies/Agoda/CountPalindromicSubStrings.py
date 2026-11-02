'''
Question — Count palindromic substrings
Problem: Count all substrings that are palindromes. Count repeated occurrences separately.

Example:
Input: s = "abc"
Output: 3
Explanation: The palindromic substrings are "a", "b", and "c".

Input: s = "aaa"
Output: 6
Explanation: The palindromic substrings are "a", "a", "a", "aa", "aa", and "aaa".

Approach:
1. Iterate through each character in the string and consider it as the center of a palindrome.
2. Expand around the center for both odd-length and even-length palindromes.
3. Count each valid palindrome found during the expansion.
4. Return the total count of palindromic substrings.

Why this works:
The algorithm works by considering each character (and the gap between characters) as the center of a potential 
palindrome and expanding outwards. 
This ensures that all palindromic substrings are counted, including those of odd and even lengths.

Time Complexity: O(n^2), where n is the length of the string.
Space Complexity: O(1), as we only use a constant amount of extra space.
'''

def count_palindromic_substrings(s):
    def expand_around_center(left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    total_count = 0
    for i in range(len(s)):
        total_count += expand_around_center(i, i)     # Odd-length palindromes
        total_count += expand_around_center(i, i + 1) # Even-length palindromes
    return total_count

# Example usage:
s = "abc"
print(count_palindromic_substrings(s))  # Output: 3

s = "aaa"
print(count_palindromic_substrings(s))  # Output: 6

'''
Find the longest palindromic substring. Instead of counting each palindrome, track the longest interval found during expansion.

Approach:
1. Iterate through each character in the string and consider it as the center of a palindrome.
2. Expand around the center for both odd-length and even-length palindromes.
3. Track the start and end indices of the longest palindrome found during the expansion.
4. Return the substring corresponding to the longest palindrome.

'''
def longest_palindromic_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    start, end = 0, 0
    for i in range(len(s)):
        left1, right1 = expand_around_center(i, i)     # Odd-length palindromes
        left2, right2 = expand_around_center(i, i + 1) # Even-length palindromes

        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2

    return s[start:end + 1]

# Example usage:
s = "babad"
print(longest_palindromic_substring(s))  # Output: "bab" or "aba"

s = "cbbd"
print(longest_palindromic_substring(s))  # Output: "bb"