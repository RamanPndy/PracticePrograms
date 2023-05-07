t = 0
while True:
    try:
        a,b = map(int, raw_input().split())
    except:
        break
    if a>b:
        a,b=b,a
    d = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    t += 1
    for i in range(a,b+1):
        while i >0:
            c = i % 10
            d[c]+=1
            i = i / 10

    str = "Case %d: %d:%d %d:%d %d:%d %d:%d %d:%d %d:%d %d:%d %d:%d %d:%d %d:%d"%(t,0,d[0],1,d[1],2,d[2],3,d[3],4,d[4],5,d[5],6,d[6],7,d[7],8,d[8],9,d[9])
    print str
    d.clear()