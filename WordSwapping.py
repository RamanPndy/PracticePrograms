t = int(raw_input())
for i in range(t):
    str = raw_input().split()
    d =[]
    for j in reversed(str):
        d.append(j)
    print ' '.join(d)