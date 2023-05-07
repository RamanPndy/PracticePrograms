# print all permutations of a string
l = list()
def permutation(str,step = 0):
    if step == len(str):
        t = ''.join(str)
        print t,
        l.append(t)

    # everything to right of step is not swapped yet
    for i in range(step,len(str)):
        str_copy = [c for c in str]

        # swap the current index with the step
        p = str_copy[step]
        q = str_copy[i]
        p,q = q,p

        # recurse on the portion of the string that has not been swapped yet
        permutation(str_copy,step+1)

permutation('abcdefghi')
print len(l)