def selectionSort(a):
    for i in range(len(a)-1,0,-1):
        posOfMax = 0
        for j in range(1,i):
            if a[j] > a[posOfMax]:
                posOfMax = j
        a[i],a[posOfMax] = a[posOfMax],a[i]
    return a
def lis(a):
    n = len(a)
    l = [1]*n
    t = list()
    d = {}

    for i in range(1,n):
        for j in range(i):
            if a[i]>a[j] and l[i] < l[j]+1:
                l[i] = l[j] + 1

    for i in range(len(l)):
        if l[i] not in d:
            d[l[i]] = [i]
        else:
            d[l[i]].append(i)
    for i in d.keys():
        c = d[i].pop(0)
        t.append(a[c])

    print t
    return len(t)
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print lis(arr2)