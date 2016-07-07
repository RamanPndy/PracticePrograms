a = "4544455455444445454455"

kases = int(raw_input())
for i in range(kases):
    n = int(raw_input())
    b = a[n-1]
    if(b == "4"):
        print "Hacker"
    else:
        print "Earth"