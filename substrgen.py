#Generate distinct substrings from a string
def substr(string):
    j = 1
    a = set()
    while True:
        for i in range(len(string)-j+1):
            a.add(string[i:i+j])
        if j == len(string):
            break
        j += 1
    return a

def prnt(seta):
    l = list(seta)
    l.sort(key=lambda (x):len(x))
    print l

def get_all_substring(string):
    length = len(string)
    alist = []
    for i in range(length):
        for j in range(i,length):
            alist.append(string[i:j+1])
    return alist

s = "raman"
print get_all_substring(s)