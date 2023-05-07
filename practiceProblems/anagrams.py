from collections import defaultdict
def anagrams(arr):
    anar = defaultdict(list)

    for w in arr:
        anar[sorted(w)].append(w)

    for g in anar.values():
        print (g)