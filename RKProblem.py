t = int(raw_input())
for i in range(t):
    str = raw_input()
    l = []
    count = []
    for j in range(len(str)):
        for k in range(j+1,len(str)+1):
            s = str[j:k]
            l.append(s)
    for j in set(l):
        c = 0
        for k in j:
            pass


