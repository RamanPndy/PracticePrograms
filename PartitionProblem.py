def partition(a):
    s = sum(a)

    if not s%2 == 0:
        return False
    else:
        n = len(a)
        part = [[0 for x in range(s/2 + 1)]for x in range(n+1)]

        for i in range(n+1):
            part[0][i] = True

        for i in range(1,s/2 +1):
            part[i][0] = False

        for i in range(1,s/2 +1):
            for j in range(1,n+1):
                part[i][j] = part[i][j-1]
                if i >= a[j-1]:
                    part[i][j] = part[i][j] or part[i-a[j-1]][j-1]

