import operator
N = int(raw_input())
l = map(int,raw_input().split())
d = []
v = []
for i in range(len(l)):
    j = i
    while j<len(l):
        t = l[i:j+1]
        d.append(t)
        j += 1
for i in range(len(l)):
    for j in range(len(l)):
        if i==j:
            continue
        else:
            d.append([l[i],l[j]])
print d
for id,val in enumerate(d):
    v.append(reduce(operator.xor,val))
print v
dp = [[0 for x in range(len(v))]for x in range(len(v))]
