import sys
T = int(raw_input())

def is_prime(a):
    x = True
    for i in range(2, a):
       if a%i == 0:
           x = False
           break
    if x:
        return x

def getPrimes(L,R):
    l = list()
    for i in range(L,R+L):
        if is_prime(i):
            l.append(i)
    return l

for i in range(T):
    numbers = map(int,raw_input().split())
    L,R = numbers[0],numbers[1]

    if L <5:
        sys.exit(0)

    else:
        S = list()
        primes = getPrimes(L,R)
        # print primes
        for j in range(len(primes)):
            if j == len(primes)-1:
                break
            else:
                p1,p2 = primes[j],primes[j+1]
                # print p1,p2
                for k in range(p2):
                    N = str(k)+str(p1)
                    if int(N) % p2 == 0:
                        S.append(N)
        print sum(map(int,S))