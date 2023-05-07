N = int(raw_input())
fact = 1
if N<0:
    print "Not Possible"
elif N ==0:
    print 0
else:
    for i in range(1,N+1):
        fact = fact*i

print str(fact).count("0")