def lbs(a):
    n = len(a)
    lis = [1 for x in range(n+1)]
    lds = [1 for x in range(n+1)]

    # compute LIS values from left to right
    for i in range(1,n):
        for j in range(i):
            if a[i] > a[j] and lis[i] < lis[j]+1:
                lis[i] = lis[j]+1

    # compute LDS values from right to left
    for i in reversed(range(n-1)):
        for j in reversed(range(i-1,n)):
            if a[i] > a[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1

    maximum = lis[0]+lds[0]+1
    for i in range(1,n):
        maximum = max((lis[i]+lds[i-1]),maximum)
    return maximum

arr =  [0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13,
        3, 11 , 7 , 15]
print "Length of LBS is",lbs(arr)