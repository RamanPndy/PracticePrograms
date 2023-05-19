'''
Input: arr[] = {5, 5, 10, 100, 10, 5}
Output: 110
Explanation: Pick the subsequence {5, 100, 5}.
The sum is 110 and no two elements are adjacent. This is the highest possible sum.

excl stores the value of the maximum subsequence sum till i-1 when arr[i-1] is excluded
incl stores the value of the maximum subsequence sum till i-1 when arr[i-1] is included.
The value of excl for the current state( say excl_new) will be max(excl ,incl). And the value of incl will be updated to excl + arr[i].
'''
def max_sum(arr):
    incl = arr[0]
    excl = 0
    for i in range(len(arr)):
        excl_new = max(incl, excl)
        incl = excl + arr[i]
        excl = excl_new
    return max(incl, excl)