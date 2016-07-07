l = [1,2,3,4,5]

def listSumItr(l):
    if not l:
        return 0
    s = 0
    for i in l:
        s += i
    return s

sumItr = listSumItr(l)
print sumItr

def listSumRecSim(l):
    if not l:
        return 0
    else:
        return l[0] + listSumItr(l[1:])

def permutations(word):
    if len(word) == 1:
        return word
