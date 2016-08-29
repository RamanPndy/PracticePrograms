
# This Program is used to calculate the minimum cost required to make the two string identical
def lcs(X,Y):
    m = len(X)
    n = len(Y)

    l = [[0 for x in range(n+1)]for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                l[i][j] = 0
            elif X[i-1] == Y[j-1]:
                l[i][j] = l[i-1][j-1]+1
            else:
                l[i][j] = max(l[i-1][j],l[i][j-1])
    print l
    index = l[m][n]
    lcsub = [""]*(index+1)
    lcsub[index] = "\0"

    i = m
    j = n

    while i>0 and j>0:
        if X[i-1] == Y[j-1]:
            lcsub[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif l[i-1][j] > l[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcsub)

def calculateCost(X,Y,costX,costY):
    m = len(X)
    n = len(Y)
    commonStr = lcs(X,Y)
    l = len(commonStr)-1

    cost = costX *(m-l) + costY * (n-l)

    return cost

X = "ef"
Y = "gh"
costX = 10
costY = 20
print calculateCost(X,Y,costX,costY)