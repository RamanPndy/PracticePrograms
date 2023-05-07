def knapsack(W,val,wt):
    n = len(val)

    k = [[0 for x in range(W+1)]for x in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif wt[i-1]<=j:
                k[i][j]  = max(val[i-1]+k[i-1][j-wt[i-1]],k[i-1][j])
            else:
                k[i][j]  = k[i-1][j]

    return k[n][W]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
print knapsack(W,val,wt)