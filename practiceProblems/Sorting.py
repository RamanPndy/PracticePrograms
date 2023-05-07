a = [5,1,7,9,3,6,2,4,8]

def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a
print bubbleSort(a)

def insertionSort(a):
    for i in range(1,len(a)):
        pos = i-1
        curr = a[i]
        while pos >= 0 and a[pos] > curr:
            a[pos] =a[pos-1]
            pos = pos-1
        a[pos+1] = curr
    return a
print insertionSort(a)

def selectionSort(a):
    for i in range(len(a)-1):
        posOfMax = i
        for j in range(i+1,len(a)):
            if a[j] < a[posOfMax]:
                posOfMax = j
        a[i],a[posOfMax]=a[posOfMax],a[i]
    return a
print selectionSort(a)
