import math

if __name__ == "__main__":
    M = 1299709
    l,q = map(int,raw_input().split())
    arr = [None]*l

    for i in range(l):
        arr[i] = [None]*int(math.pow(2,i))

    print arr
    arr[l-1][0] = 1
    print arr
    for i in range(1,int(math.pow(2,l-1))):
        arr[l-1][i] = arr[l-1][i-1] + 1

    print arr
    j = l-2
    while(j >=0):
        temp = 0

        for k in range(int(math.pow(2,j))):
            temp += 1
            arr[j][k] = arr[j+1][temp]*arr[j+1][temp]
        j -= 1

    print arr
    sum = [0]*q
    for i in range(q):
        # n = int(raw_input())
        # x = int(raw_input())
        # y = int(raw_input())
        numbers = map(int, raw_input().split())
        n = numbers[0]
        x = numbers[1]
        y = numbers[2]

        x -= 1
        while(x<y):
            sum[i] = (sum[i] + arr[n-1][x]) % M
            x += 1

    for i in range(q):
        print sum[i]