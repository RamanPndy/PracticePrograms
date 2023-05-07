# Greedy
def minNoOfCoins(V,coins):
    coins = sorted(coins)[::-1]
    c = 0
    l = []
    for i in range(len(coins)):
        if V >= coins[i]:
            V = V - coins[i]
            c += 1
            l.append(coins[i])
    print l
    return c

coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
N = 93
print minNoOfCoins(N,coins)