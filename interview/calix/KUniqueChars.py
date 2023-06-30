'''
To solve the problem, we can use a sliding window approach to find the longest substring with k unique characters. We'll use a hashmap to keep track of the character frequencies within the sliding window. Whenever the number of unique characters in the window exceeds k, we'll adjust the window by moving the left pointer until the window contains only k unique characters again. We'll keep track of the longest substring encountered during the process and return it at the end.
'''
def KUniqueCharacters(str):
    k = int(str[0])
    str = str[1:]  # Remove the first character (k) from the string
    n = len(str)
    if n < k:
        return ""

    left, right = 0, 0
    max_length = 0
    max_substring = ""

    # Dictionary to keep track of character frequencies within the window
    char_freq = {}

    while right < n:
        # Expand the window to the right
        char = str[right]
        char_freq[char] = char_freq.get(char, 0) + 1

        # Shrink the window from the left if the number of unique characters exceeds k
        while len(char_freq) > k:
            left_char = str[left]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            left += 1

        # Check if the current window is the longest encountered so far
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
            max_substring = str[left:right + 1]

        right += 1

    return max_substring


# Test cases
print(KUniqueCharacters("2aabbacbaa"))  # Output: "aabba"
