a = [2,5,8,4,6,2,8,7,9,5]

def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

a = bubbleSort(a)
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        continue
    else:
        print a[i],