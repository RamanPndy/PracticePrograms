def lcs(X,Y,m,n):
    if m ==0 or n==0:
        return 0
    elif X[m-1] == Y[n-1]:
        return lcs(X,Y,m-1,n-1) + 1
    else:
        return max(lcs(X,Y,m-1,n),lcs(X,Y,m,n-1))
