a = [1,2,3,4]

def appendImpl(a,v):
    s = len(a)
    newl = [0]*(s+1)
    for i in range(s):
        newl[i] = a[i]
    newl[len(newl)-1] = v
    a = newl
    return a
# a = appendImpl(a,5)
def popImpl(a):
    s = len(a)
    newl = [0]*(s-1)
    for i in range(s-1):
        newl[i] = a[i]
    a = newl
    print id(a)
    print id(newl)
    return a
a = popImpl(a)
print id(a)
print a
