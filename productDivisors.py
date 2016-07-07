N = int(raw_input())

numbers = map(int, raw_input().split())

a = list()
l = list()
def len_factors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            # prin
            l.append(i)
    return len(l)


for i in range(N):
    a.append(numbers[i])

p = 1

for i in a:
    p*= i
# print p
print len_factors(p)
