def MCM(a):
    n = len(a)

    m = [[0 for x in range(n)]for x in range(n)]

    for i in range(n):
        m[i][i] = 0

    for l in range(2,n):
        for i in range(1,n-l+1):
            j = i-l+1
            m[i][j] = 32767

            for k in range(i,j):
                q = m[i][k]+m[k+1][j]+a[i-1]*a[k]*a[j]

                if q<m[i][j]:
                    m[i][j] = q
    return m[1][n-1]
