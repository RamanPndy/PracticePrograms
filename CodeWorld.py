M = 10**9+7
t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    l = [i+1 for i in range(n)]
    d = []
    a=[]
    # print l
    for j in range(len(l)-1):
        for k in range(j+1,len(l)):
            s = [l[j],l[k]]
            d.append(s)
    # print d
    for j in range(len(l)):
        for k in d:
            if l[j] in k:
                pass
            else:
                b = [k,l[j]]
                a.append(b)
    # print a
    if len(l) == 1:
        print 1
    elif len(l) == 2:
        print 2
    else:
        print (len(a) + 1)%M