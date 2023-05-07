cases = int(raw_input())

coords = []

# getting coordinates for all the cases
for i in range(cases):
    temp = []
    for j in range(4):
        temp.append(raw_input().split())

    coords.append(temp)

print coords
for i in range(cases):
    # x-coords
    ax = coords[i][0][0]
    bx = coords[i][1][0]
    cx = coords[i][2][0]
    dx = coords[i][3][0]
    # y-coords
    ay = coords[i][0][1]
    by = coords[i][1][1]
    cy = coords[i][2][1]
    dy = coords[i][3][1]

    # If any three are on a single line
    if ax == bx == cx or ax == cx == dx or bx == cx == dx or ax == bx == dx:
        print "Yes"
        continue
    if ay == by == cy or ay == cy == dy or by == cy == dy or ay == by == dy:
        print "Yes"
        continue

    # if B-D or A-C are not properly crossing each other
    '''if bx != dx and by != dy:
        print "Yes"
        continue
    if ax != cx and ay != cy:
        print "Yes"
        continue'''

    # find whether B-D have same x-coord or same y-coord,then check for range
    cobdx = False
    if bx == dx:
        cobdx = True

    '''coacx = False
    if ax == cx:
        coacx = True'''

    if cobdx:
        if not ((bx >= ax and bx <= cx) or (bx >= cx and bx <= ax)):
            print "Yes"
            continue
        if not ((ay >= by and ay <= dy) or (ay <= by and ay >= dy)):
            print "Yes"
            continue

    print "No"
