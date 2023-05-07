a = [31,14,15,7,2]
b = []
c = []
e = []
f = []
for id,i in enumerate(a):
    b.append(bin(i).count("1"))
    c.append(id)

d = [x for (y,x) in sorted(zip(b,c))]

for i in d:
    e.append(a[i])

for id,i in enumerate(e):
    if id != (len(e)-1):
        if (bin(e[id]).count("1") == bin(e[id+1]).count("1")):
            e[id],e[id+1] = e[id+1],e[id]

for i in reversed(e):
    f.append(i)

print f

