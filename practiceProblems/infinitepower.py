t = int(raw_input())

def checkUnlimitedPower(n):
    n = str(n)
    t = 0
    for j in n:
        if int(j)%2 != 0:
            pass
        else:
            t += 1

    if t == len(n):
        return 1
    else:
        return 0

for i in range(t):
    n = int(raw_input())

    c = checkUnlimitedPower(n)

    if c == 1:
        print "Unlimited Power"
    else:
        t1 = n
        while not checkUnlimitedPower(t1):
            t1 += 1

        t2 = n
        while not checkUnlimitedPower(t2):
            t2 -= 1

        n1 = abs(t1-int(n))
        n2 = abs(t2-int(n))

        if n1 % n2 == 0 :
            print str(n1/n2) + "/1"
        else:
            print str(n1)+ "/"+str(n2)

