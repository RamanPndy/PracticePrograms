N = int(raw_input())
names = list()
out = list()
for i in range(N):
    name = raw_input()
    names.append(name)

print names

cnt = 0
for i in range(len(names)):
    for j in range(len(names)):
        if names[j] == names[i]:
            pass
        elif sorted(names[j]) == sorted(names[i]):
            l = list()
            l.append(names[i])
            l.append(names[j])
            out.append(l)

print out
