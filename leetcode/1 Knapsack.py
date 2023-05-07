# recursive implementation of 0/1 knapsack problem
def knapsack(W,wt,val,n):
    # return the maximum value that can be put in a knapsack of weight W.
    # Base Case
    if n==0 or W==0:
        return 0

    # if weight of the nth item is greater than W then it would not be included in the optimal solution
    if (wt[n-1] > W):
        return knapsack(W,wt,val,n-1)

    # return the maximum of two cases
    # 1.nth item included
    # 2.nth item not included

    else:
        return max(val[n-1] + knapsack(W-wt[n-1],wt,val,n-1),knapsack(W,wt,val,n-1))

val = [60,100,120]
wt = [10,20,30]
W =50
n = len(val)

print (knapsack(W,wt,val,n))
