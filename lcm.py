N = int(raw_input())

numbers = []
lcm = []


for i in range(1,N+1):
    numbers.append(i)

while len(numbers) > 0:
    t = 1
    numbers2 = list()
    for i in reversed(numbers):
        numbers2.append(i)
    # print numbers2
    for i in range(len(numbers2)):
        for j in range(i+1,len(numbers2)):
            if numbers2[i] % numbers2[j] == 0:
                numbers2[i] = numbers2[i] / numbers2[j]
    for k in numbers2:
        t = t*k
    lcm.append(t)
    # print lcm
    numbers.pop(0)
    # print numbers
    del numbers2

# print lcm

c = 0
for i in range(len(lcm)):
    for j in range(i+1,len(lcm)):
        if lcm[i] == lcm[j]:
            c += 1

print c