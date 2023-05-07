t = int(raw_input())
for i in range(t):
    N = int(raw_input())
    shop =[[0 for x in range(3)]for x in range(N)]
    for j in shop:
        j[0],j[1],j[2] = map(int,raw_input().split())
    # print shop
    d = [[0 for x in range(3)]for x in range(N)]

    for j in range(3):
        d[0][j] = shop[0][j]

    # print d

    for j in range(1,N):
        d[j][0] = min(d[j-1][1],d[j-1][2])+shop[j][0]
        d[j][1] = min(d[j-1][0],d[j-1][2])+shop[j][1]
        d[j][2] = min(d[j-1][0],d[j-1][1])+shop[j][2]

    m = min(min(d[N-1][0],d[N-1][1]),d[N-1][2])

    print m