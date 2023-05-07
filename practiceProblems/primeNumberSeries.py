def isPrime(num):
    t = False
    for i in range(2,num):
        if num % i ==0:
            t = True
        if t:
            break
    if t:
        return False
    else:
        return True

def getPrimeSeries(a,b):
    l = list()
    for i in range(a,b+1):
        if isPrime(i):
            l.append(i)
    print l
    return l

def getEachDigit(n):
    l = list()
    while n!=0:
        t = n%10
        l.append(t)
        n = n/10
    return l

def getFrequentMost(a,b):
    l = getPrimeSeries(a,b)
    d = {}
    s = 0
    for i in l:
        t = getEachDigit(i)
        for j in t:
            if j not in d.keys():
                d[j] = 0
    print d
    for i in l:
        t = getEachDigit(i)
        for j in t:
            if j in d.keys():
                d[j] += 1
    print d
    print max([x for x in d.values()])

getFrequentMost(5,15)
