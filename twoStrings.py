T = int(raw_input())
for i in range(T):
    A = raw_input()
    B = raw_input()

    d = list()

    d.append(A)
    j = 0
    while j != len(A):
        for k in range(len(A)):
            t = A[k:k+j]
            d.append(t)
        j += 1

    t = False
    for l in d:
        if l == '':
            continue
        if l in B:
            t = True
            break
    if t:
        print "YES"
    else:
        print "NO"