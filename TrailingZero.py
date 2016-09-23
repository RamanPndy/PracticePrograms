t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    c = 0
    j = 5
    while(n/j >=1):
        c += n/j
        j *= 5
    print c
