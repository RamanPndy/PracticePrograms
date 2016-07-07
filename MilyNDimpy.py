N = int(raw_input())
numbers = map(int, raw_input().split())
l = list()
for i in range(N):
    l.append(numbers[i])

# print l
s = list()

for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if j < len(l):
            if l[i] == l[j]:
                s.append(j)

new = l[:]

for x in s:
    new[x] = 'J'

ln= []
for i in new:
    if i  in l:
       ln.append(i)

for i in ln:
    print i,
