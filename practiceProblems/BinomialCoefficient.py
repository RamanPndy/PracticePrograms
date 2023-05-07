def binomialCoefficient(n,k):
    c = [[0 for x in range(k+1)]for x in range(n+1)]

    for i in range(n+1):
        for j in range(min(i,k)+1):
            if i==0 or j==0:
                c[i][j] = 1
            else:
                c[i][j] = c[i-1][j-1] + c[i-1][j]

    return c[n][k]
print binomialCoefficient(5,2)