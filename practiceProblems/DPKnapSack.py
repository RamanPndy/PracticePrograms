def knapsack(W,wt,val):
    # Program to find the 0/1 knapsack solution using dynamic programming
    n = len(wt)
    K = [[0 for x in range(W + 1)]for x in range(n + 1)]

    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                K[i][j] = 0
            elif wt[i-1] > j:
                K[i][j] = max(val[i-1]+K[i-1][j-wt[i-1]],K[i-1][j])
            else:
                K[i][j] = K[i-1][j]