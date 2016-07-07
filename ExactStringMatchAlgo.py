def find_occurrences(t,p):
    lt,lp = len(t),len(p)
    for i in range(lt-lp+1):
        match = True
        for l in range(lp):
            if t[i+l] != p[l]:
                match = False
                break
        if match:
            print(i)

find_occurrences('ramanamuudfujamijifdfamisifjisam','am')
