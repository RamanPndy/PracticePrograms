kases = int(raw_input())
for kase in range(kases):
    N = int(raw_input())
    result = 1
    for i in range(1, N + 1):
        result = result * i
    print result