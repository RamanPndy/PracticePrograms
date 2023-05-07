INT_MIN = -32767

def cutRod(a):
    n = len(a)
    val = [0 for x in range(n)]
    val[0] = 0

    for i in range(1,n+1):
        maxVal =INT_MIN
        for j in range(i):
            maxVal = max(maxVal,a[j]+val[i-j-1])
        val[i] = maxVal

    return val[n]

arr = [1, 5, 8, 9, 10, 17, 17, 20]
print cutRod(arr)