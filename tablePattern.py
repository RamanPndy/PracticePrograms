n = int(raw_input())

l = [1]

for i in range(1,n):
    if i%3 == 0:
        l.append(i)

for i in range(1,len(l)):
    for j in range(i):
        print l[j],
    print '\n',
