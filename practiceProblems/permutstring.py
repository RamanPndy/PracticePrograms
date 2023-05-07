def toString(List):
    return ''.join(List)

def permute(a, l, r):
    if l==r:
        print toString(a),
    else:
        for i in xrange(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack

string = "hat"
n = len(string)
a = list(string)
print permute(a, 0, n-1)
