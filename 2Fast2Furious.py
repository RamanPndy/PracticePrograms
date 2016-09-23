N = int(raw_input())
D = map(int,raw_input().split())
B = map(int,raw_input().split())
dom = []
brian = []
for i in range(N-1):
    dom.append(abs(D[i]-D[i+1]))
    brian.append(abs(B[i]-B[i+1]))
d=max(dom)
b=max(brian)
if d==b:
    print "Tie"
    print 0
elif d>b:
    print "Dom"
    print d
else:
    print "Brian"
    print b