def binarySearch(A,x):
    # Program to find out the element x in array A using binary search
    first = 0
    last = len(A)-1
    mid = -1
    while first<=last:
        mid = (first + last)//2
        if A[mid] == x:
            return mid
        else:
            if x < A[mid]:
                last = mid-1
            else:
                first = mid+1

    return mid

def binarySearchFirstOccurence(A,x):
    # Program to find the first occurrence of element x in array A using binary Search
    first = 0
    last = len(A) - 1
    result = -1
    while first <= last:
        mid = (first+last)/2
        if A[mid] == x:
            result = mid
            last = mid-1
        else:
            if x < A[mid]:
                last = mid -1
            else:
                first = mid + 1
    return result

def binarySearchLastOccurence(A,x):
    # Program to find the last occurrence of element x in array A using binary search
    first = 0
    last = len(A) - 1
    result = -1
    while first <= last:
        mid = (first + last)/2
        if A[mid] == x :
            result = mid
            first = mid +1
        else:
            if x < A[mid]:
                last = mid -1
            else:
                first = mid +1
    return result

def countAllOccurrence(A,x):
    # Program to find all occurrence of element x in array A using binary search
    first = binarySearchFirstOccurence(A,x)
    last = binarySearchLastOccurence(A,x)
    return last - first +1
A = [2,4,4,10,10,10,15,18,18,20,20,25]
x = 15
print binarySearch(A,x)
# print binarySearchFirstOccurence(A,x)
# print binarySearchLastOccurence(A,x)
# print countAllOccurrence(A,x)