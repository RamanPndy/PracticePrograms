def lps(X,Y):
    m = len(X)
    n = len(Y)

    L = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])

    print L[m][n]
    index = L[m][n]

    l = [""]*index
    i = m
    j = n
    while i>0 and j>0:
        if X[i-1] == Y[j-1]:
            l[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j -=1
    return ''.join(l)

X = "geeksskeeg"
Y = X[::-1]
print lps(X,Y)