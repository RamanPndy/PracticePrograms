def minSubsetSum(arr):
    n = len(arr)

    sum = 0
    for i in arr:
        sum += i

    return findMinSubSet(arr, n, 0, sum)

def findMinSubSet(arr, idx, sumCalculated, sumTotal):
    if idx == 0:
        return abs((sumTotal-sumCalculated) - sumCalculated)

    return min(findMinSubSet(arr, idx-1, sumCalculated, sumTotal), findMinSubSet(arr, idx-1, sumCalculated+arr[idx-1], sumTotal))