
def get_all_substring(string):
    length = len(string)
    alist = []
    for i in range(length):
        for j in range(i,length):
            alist.append(string[i:j+1])
    return alist
def  funPal( s):
    lst = get_all_substring(s)
    lst2 = []
    for i in lst:
        lst2.append(len(i))

    lst3 = []
    for j in lst2:
        for k in lst2:
            lst3.append(k*j)
    return max(lst3)

res = funPal('raman')
print res