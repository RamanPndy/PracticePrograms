def orientation(p, q, r):
    val = (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
    return val

T = int(raw_input())
A = list()
for i in range(0,T):
    for j in range(0,4):
        for x in raw_input().split():
            A.append(int(x))
    p1 = A[:2]
    p2 = A[2:4]
    q1 = A[4:6]
    q2 = A[6:8]
    A = []
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    if (o1 * o2 < 0 and o3 * o4 < 0 ):
        print "No"
    else:
        print "Yes"