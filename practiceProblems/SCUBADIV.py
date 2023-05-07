def scubaDive(MaxOxgn,MaxNitgn,WtCylndr,OVal,NVal,n):
    if n == 0 or MaxOxgn == 0 or MaxNitgn  == 0:
        return 0
    if OVal[n-1] > MaxOxgn or NVal[n-1]>MaxNitgn:
        return scubaDive(MaxOxgn,MaxNitgn,WtCylndr,OVal,NVal,n-1)
    else:
        return min(scubaDive(MaxOxgn,MaxNitgn,WtCylndr,OVal,NVal,n-1),
                   scubaDive(max(MaxOxgn-OVal[n-1],0),max(MaxNitgn-NVal[n-1],0),WtCylndr,OVal,NVal,n-1)+WtCylndr[n-1])

c = int(raw_input())
for i in range(c):
    t,a = map(int,raw_input().split())
    if (t >= 1 and t <= 21) and (a >= 1 and a <= 79):
        n = int(raw_input())
        if n >= 1 and n <= 1000:
            l = [[0 for x in range(3)]for x in range(n)]
            for j in l:
                j[0],j[1],j[2] = map(int,raw_input().split())
            # print l
            wt = [l[x][2] for x in range(n)]
            OVal = [l[x][0] for x in range(n)]
            NVal = [l[x][1] for x in range(n)]
            OorN = max(a,t)
            minWt  = scubaDive(t,a,wt,OVal,NVal,n)
            print minWt

