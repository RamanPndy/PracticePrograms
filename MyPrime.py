# a=[f(i) for f,i in zip((int, int), raw_input().split())]
# print a
#
# numbers = [int(n) for n in input().split()]
# print numbers

S = int(raw_input())
l = list()
out = list()
numbers = map(int, raw_input().split())
for i in range(S):
    l.append(numbers[i])

l.sort()
# print l

for i in range(S):
    cnt=0
    for j in l:
        if l[i]==j:
            pass
        elif l[i]%j==0:
            break
        else:
            cnt+=1

    if cnt==S-1:
         out.append(l[i])

for i in out:
    print i,




