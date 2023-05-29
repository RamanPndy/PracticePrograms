# Program to convert one string to another string
def editDistance(X,Y):
    m = len(X)
    n = len(Y)

    l = [[0 for x in range(n+1)]for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                l[i][j] = j
            elif j == 0:
                l[i][j] = i
            elif X[i-1] == Y[j-1]:
                l[i][j] = l[i-1][j-1]
            else:
                l[i][j] = 1 + min(l[i][j-1],l[i-1][j],l[i-1][j-1])
    return l[m][n]