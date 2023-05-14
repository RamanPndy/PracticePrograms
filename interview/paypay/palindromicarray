An array is called palindromic if it remains the same after reversing the order of its elements.

You have an array of strings arr. For each i, arr[i] consists of at least two characters. For each pair of consecutive elements arr[i] and arr[i + 1], you can:

Move the rightmost character of arr[i] to the leftmost position in arr[i + 1]. For instance, "abc" and "def" will become "ab" and "cdef". This operation can be applied only once to any pair of consecutive elements.
Move the leftmost character of arr[i + 1] to the rightmost position in arr[i]. For instance, "abc" and "def" will become "abcd" and "ef". Again, this operation can be applied only once to any pair of consecutive elements.
Do nothing to the pair of consecutive elements.
Is it possible to obtain a palindromic array from arr by performing these operations?

Example

For arr = ["aa", "bab", "cde", "aba", "ab"], the output should be
solution(arr) = true.

Apply the second operation to "aa" and "bab".
Apply the first operation to "aba" and "ab".
This gives us the following array: ["aab", "ab", "cde", "ab", "aab"], which is palindromic.
For arr = ["palindrome"], the output should be
solution(arr) = true.

The given array is already palindromic, so no operations are needed.

For arr = ["aaaaaa", "aa"], the output should be
solution(arr) = false.

If moving two characters between two consecutive array elements was allowed, the array could have been made palindromic, but this is impossible given the actual rules.

Input/Output

[execution time limit] 4 seconds (py)

[memory limit] 1 GB

[input] array.string arr

An array of strings.

Guaranteed constraints:
1 ≤ arr.length ≤ 105,
2 ≤ arr[i].length ≤ 10.

[output] boolean

Return true if the given array can be turned into a palindromic array, otherwise return false.