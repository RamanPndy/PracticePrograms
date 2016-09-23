N,P = map(int,raw_input().split())
p = P/100.0
q = 1-p
l = []
d = []
f = []
if N%2 == 0:
    a = (N/2)
    f.append(a*p)
if N%3 == 0:
    a = (N/3)
    f.append(a*q)
elif N >3:
    x = 0
    a = N
    while a> 2:
        a -= 2
        x += 1
        if a%3 == 0:
            a = (a/3)
            l.append([x,a])
    x = 0
    a = N
    while a>3:
        a -= 3
        x += 1
        if a%2 ==0:
            a = (a/2)
            l.append([a,x])

    # print l
    for i in l:
        if (i[0]*2+i[1]*3) == N:
            d.append(i)
    # print d
    for i in d:
        f.append((i[0]*p)*(i[1]*q))
print '%.6f'%sum(f)