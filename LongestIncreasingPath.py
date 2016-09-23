t = int(raw_input())
for i in range(t):
    N,M = map(int,raw_input().split())
    mat = [[0 for x in range(N)]for x in range(M)]
    for j in range(M):
        s = map(int,raw_input().split())
        for k in range(N):
            mat[j][k] = s[k]

    dp = [[0 for x in range(N)]for x in range(M)]
    dp[0][0] = 1
    # print dp
    for j in range(1,N):
        if mat[0][j]>mat[0][j-1]:
            dp[0][j] = dp[0][j-1] + 1
    # print dp
    for j in range(1,M):
        if mat[j][0]>mat[j-1][0]:
            dp[j][0] = dp[j-1][0] + 1
    # print dp

    for j in range(1,M):
        for k in range(1,N):
            if mat[k][j]>mat[k][j-1]:
                dp[k][j] = max(dp[k][j],dp[k][j-1]+1)
            if mat[k][j]>mat[k-1][j]:
                dp[k][j] = max(dp[k][j],dp[k-1][j]+1)
    print dp
    print dp[N-1][M-1]

