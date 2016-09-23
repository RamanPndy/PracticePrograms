l = [1,2,1,3,2,4,4,5]
d = {}
t = []
for i in range(len(l)):
    if l[i] not in d:
        d[l[i]] = [i]
    else:
        d[l[i]].append(i)

print d
for i in d.keys():
    t.append(d[i].pop(0))

print t
