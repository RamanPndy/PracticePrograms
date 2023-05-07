numbers= map(int,raw_input().split())
numbers2= map(int,raw_input().split())
d = list()
m = list()
s = 0
for i in range(numbers[0]):
    d.append(numbers2[i])

for i in range(len(d)-1):
    for j in range(i+1,len(d)):
        t1 = d[i]
        t2 = d[j]
        t = list()
        t.append(t1)
        t.append(t2)
        m.append(t)

for i in m:
    d = abs(i[0]-i[1])
    if d == numbers[1]:
        s+=1
print s
