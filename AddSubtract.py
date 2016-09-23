def addSubtract(a,K):
    d ={}
    for i in range(len(a)):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    t = [{i:d[i]} for i in sorted(d.keys())]
    print t

t = int(raw_input())
for i in range(t):
    N,K = map(int,raw_input().split())
    arr = map(int,raw_input().split())
    print addSubtract(arr,K)
