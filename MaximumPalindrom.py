def maxPalindromPartition(str):
    n = len(str)
    c = [[0 for x in range(n)]for x in range(n)]
    p = [[0 for x in range(n)]for x in range(n)]

    for i in range(n):
        c[i][i] = 0
        p[i][i] = True

    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i + l -1
            if l==2:
                p[i][j] = (str[i] == str[j])
            else:
                p[i][j] = (str[i] == str[j]) and (p[i+1][j-1])

            if p[i][j] == True:
                c[i][j] = 0
            else:
                c[i][j] = 32767
                for k in range(i,j):
                    c[i][j] = min(c[i][j],c[i][k]+c[k+1][j]+1)

    return c[0][n-1]

print maxPalindromPartition("ababbbabbababa")