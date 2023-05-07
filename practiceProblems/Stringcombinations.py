def combinations(str):
    n = len(str)
    l = []
    for i in range(n):
        j = i
        while j < n:
            s = str[i:j+1]
            l.append(s)
            j +=1
    return l
print combinations("raman")