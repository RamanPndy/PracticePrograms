a = [34, 8, 10, 1, 2, 80, 30, 33, 1]
n = len(a)
index = dict()

for i in range(n):
    if a[i] in index:
        index[a[i]].append(i)
    else:
        index[a[i]] = [i]

print (index)
a.sort()

maxDiff = 0

temp = n

for i in range(n):
    if temp > index[a[i]][0]:
        temp = index[a[i]][0]

    maxDiff = max(maxDiff, index[a[i]][-1] - temp)

print (maxDiff)
