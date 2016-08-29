def lcs(exp1,exp2):
    m = len(exp1)
    n = len(exp2)
    print m,n
    L = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j == 0:
                L[i][j] = 0
            elif exp1[i-1] == exp2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])

    print L
    index = L[m][n]

    lcsub = [""]*(index+1)
    lcsub[index] = "\0"

    i = m
    j = n

    while i>0 and j >0:
        if exp1[i-1] == exp2[j-1]:
            lcsub[index-1] = exp1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    print "".join(lcsub)
a = 'AGGTAB'
b = 'GXTXAYB'
lcs(a,b)
