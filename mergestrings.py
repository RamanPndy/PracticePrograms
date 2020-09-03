def mergestrings(str1, str2):
    flag = 0
    c =[]
    for i in range(len(str1)):
        if str1[i] == str2[0]:
            c.append(i)
    print c
    for i in c:
        if str1[i:] == str2[:len(str1)-i]:
            str1 = str1 + str2[len(str1)-i]
            print (str1)
            flag=1
            break
    if flag == 0:
        print (str1 + str2)

mergestrings("roadshow", "showman")