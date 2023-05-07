t = 2
l = list()

for i in range(t):
    numbers = map(int, raw_input().split())
    for j in numbers:
        l.append(j)

print l