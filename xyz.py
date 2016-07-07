a = [1,2,3,4]
b = [2,4,1,3]
d = [6,0,2,8]

c = 0
l = list()

while c != len(a):
    if a[c] > b[c]:
        l.append(a[c])
    else:
        l.append(b[c])

    c += 1

print l

print zip(a,b)

print [max(x) for x in zip(a,b) ]

d1 = {"name":"raman","age":23}
d2 = {"sex":"male","mob":"hkh"}

t = lambda x:x*x

print t(2)