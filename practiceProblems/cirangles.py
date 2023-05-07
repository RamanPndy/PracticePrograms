tc = int(raw_input())
cir = []
for i in range(tc):
    D,F,S,K = map(int,raw_input().split())

    # print D,F,S,K
    for j in range(1,K+1):
        t = [None]*j
        cir.append(t)

    noc = 0
    for k in cir:
        noc += len(k)

    if noc != (D+F+S):
        print 0
    else:
        print 1







