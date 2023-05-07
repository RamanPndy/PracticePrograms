import itertools
N = int(raw_input())

numbers = map(int,raw_input().split())

l = list()

for i in range(N):
    l.append(numbers[i])


p = list(itertools.permutations(l))

ml = list()

for i in p:
    lg = len(i)
    # print i
    t = 0
    for j in range(lg-1):
        # print i[j],i[j+1]
        t += abs(i[j] - i[j+1])
    ml.append(t)

print max(ml)

