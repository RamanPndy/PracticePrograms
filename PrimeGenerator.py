def checkPrime(n):
    t = False
    if n <2:
        return t
    for i in range(2,n):
        if n % i ==0:
            t = True
            break
    if t:
        return False
    else:
        return True
t = int(raw_input())
for i in range(t):
    m,n =map(int,raw_input().split())
    for j in range(m,n+1):
        if checkPrime(j):
            print j