t = int(raw_input())
for i in range(t):
    N = int(raw_input())
    p = map(int,raw_input().split())
    c = 0
    for j in range(N):
        for k in range(N):
            if j == k:
                continue
            if p[j] & p[k] == 0:
                c+=1
    print c