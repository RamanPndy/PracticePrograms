B,V = raw_input().split(' ')
N = int(B)
M = int(V)
x = []
a = list()
for i in range(N):
    for j in range(M):
        k = raw_input()
        a.append(int(k))

    x.append(a)

print x

rowS = []
colS = []

for i in x:
    rowS.append(sum(i))

# print rowS

y = [[] for k in range(len(x[0]))]
for i in x:
    for id,j in enumerate(i):
        y[id].append(j)
    colS.append(y)

colSum = colS[0]
# print colSum

z = []
for i in colSum:
    z.append(sum(i))

# print z

XOR = []

for i in rowS:
    for j in z:
        XOR.append(i^j)

# print XOR

print max(XOR)