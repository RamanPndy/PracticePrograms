cost = []
q = int(raw_input())
for i in range(q):
    query = map(int,raw_input().split())
    if query[0] == 1:
        if len(cost) == 0:
            print "No Food"
        else:
            print cost.pop()
    elif query[0] == 2:
        cost.append(query[1])