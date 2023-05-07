# Memoization : Top-Down
def fib(n,lookup):

    #Base case n == 0 or n == 1:
    if n == 0 or n == 1:
        lookup[n] = n

    #If the value is not calculated , then calculate t
    if lookup[n] is None:
        lookup[n] = fib(n-1,lookup) + fib(n-2,lookup)

    return lookup[n]

lookup = [None]*100
print fib(34,lookup)