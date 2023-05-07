def lis(a):
    n = len(a)
    max = 0
    msis = [0 for x in range(n)]

    for i in range(n):
        msis[i] = a[i]

    for i in range(1,n):
        for j in range(i):
            if a[i] > a[j]  and msis[i] < msis[j] + a[i]:
                msis[i] = msis[j] + a[i]

    for i in range(n):
        if max < msis[i]:
            max = msis[i]

    return max
arr = [1, 101, 2, 3, 100, 4, 5]
print lis(arr)
