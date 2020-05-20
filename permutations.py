def permutations(strign):
    perms = set()
    n = len(strign)
    arr = list(strign)
    for i in range(n):
        j = n - 1
        while j != 0:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            perms.add("".join(arr))
            j -= 1
    return perms

def getallperms(strign):
    initperms = permutations(strign)
    p = []
    for i in initperms:
        print (i)
        p.append(permutations(i))
    return p