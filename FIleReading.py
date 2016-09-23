with open("common pledge.txt","rt") as inFile:
    str = inFile.read()

l = str.split(" ")
d = {}
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 2
# print d
