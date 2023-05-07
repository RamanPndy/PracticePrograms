N = int(raw_input())
s = raw_input()
if len(s) != N:
    exit(0)

Q = list()
ss = list()

for i in range(N):
    for j in range(N):
        ss.append(s[i:j+1])

ls = set(ss)
# print ls
NQ = int(raw_input())

for i in range(NQ):
    occurence = 0
    q = raw_input()
    Q.append(q)
    X,Y = q.split()

    for k in ls:
        if k.startswith(X) and k.endswith(Y):
            occurence += 1
        elif k.startswith(Y) and k.endswith(X):
            occurence += 1
    print occurence


