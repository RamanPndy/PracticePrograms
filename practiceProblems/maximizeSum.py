T = int(raw_input())
l = list()
d = list()
for i in range(T):
    numbers = map(int,raw_input().split())
    numbers2 = map(int,raw_input().split())
    for j in range(numbers[0]):
        l.append(numbers2[j])

    # print numbers,l
    # d.append(l)
    j = 0
    while j != len(l):
        for i in range(len(l)):
            t = l[i:i+j]
            d.append(t)
        j += 1

    print max([sum(k) % numbers[1] for k in d])
