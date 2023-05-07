def coinChange(S,n):
    m  = len(S)

    tc = [[0 for x in range(m)]for x in range(n+1)]

    for i in range(m):
        tc[0][i] = 1

    for i in range(1,n+1):
        for j in range(m):
            # count of solutions including S[j]
            x = tc[i-S[j]][j] if i-S[j] >=0  else 0

            # count of solutions excluding S[j]
            y = tc[i][j-1] if j >=1 else 0

            # total count

            tc[i][j] = x +y

    t = tc[n][m-1]
    return t

arr = [1, 2, 3]
n = 4
print coinChange(arr,n)
