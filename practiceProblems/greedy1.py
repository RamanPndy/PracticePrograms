t = int(raw_input())
for i in range(t):
    N,X = raw_input().split()
    bottles = list()
    bt = map(int,raw_input().split())
    for j in range(int(N)):
        bottles.append(bt[j])

    currentCapacity = 0
    numberOfBottles = list()
    bottles.sort()
    # print bottles

    for i in bottles:
        if currentCapacity <= int(X):
            currentCapacity += i
            numberOfBottles.append(bottles.pop())

    print len(numberOfBottles)