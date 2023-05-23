
# Expand in both directions of `low` and `high` to find all palindromes
def expand(s, low, high, palindromes):
 
    # run till `s[low.high]` is not a palindrome
    while low >= 0 and high < len(s) and s[low] == s[high]:
 
        # push all palindromes into a set
        palindromes.add(s[low: high + 1])
 
        # Expand in both directions
        low = low - 1
        high = high + 1
 
 
# Function to find all unique palindromic substrings of a given string
def findPalindromicSubstrings(s):
 
    # create an empty set to store all unique palindromic substrings
    palindromes = set()
 
    for i in range(len(s)):
 
        # find all odd length palindrome with `s[i]` as a midpoint
        expand(s, i, i, palindromes)
 
        # find all even length palindrome with `s[i]` and `s[i+1]`
        # as its midpoints
        expand(s, i, i + 1, palindromes)
 
    # print all unique palindromic substrings
    print(palindromes)