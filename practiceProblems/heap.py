'''
Python heapq only implements minHeap by default, the standard way to create maxHeap is to multiply the elements with -1 before pushing in and, multiply with -1 after popping out.
arr[(k - 1)/2] will return the parent node

arr[(2*k) + 1] will return left child

arr[(2*k) + 2] will return right child

maxHeapify(array, size, k)
  set k as largest
  leftChild = 2k + 1
  rightChild = 2k + 2
  
  if leftChild > array[largest]
    set leftChildIndex as largest
  if rightChild > array[largest]
    set rightChildIndex as largest

  swap array[k] and array[largest]

minHeapify(array, size, k)
  set k as smallest
  leftChild = 2k + 1
  rightChild = 2k + 2
  
  if leftChild < array[smallest]
    set leftChildIndex as smallest
  if rightChild < array[smallest]
    set rightChildIndex as smallest

  swap array[k] and array[smallest]

Algorithm for Max Heap:
MaxHeap(array, size)
  loop from the first index down to zero
    call maxHeapify

Algorithm for Insertion in Max Heap:
If there is no node, 
  create a new Node.
else (a node is already present)
  insert the new Node at the end 
  
maxHeapify the array

Algorithm for Deletion in Max Heap:
If nodeDeleted is the leaf Node
  remove the node
Else swap nodeDeleted with the lastNode
  remove nodeDeleted
   
maxHeapify the array

Algorithm for Min Heap:
MinHeap(array, size)
  loop from the first index down to zero
    call minHeapify

Algorithm for Insertion in Min Heap:
If there is no node, 
  create a new Node.
else (a node is already present)
  insert the new Node at the end 
  
minHeapify the array

Algorithm for Deletion in Min Heap:
If nodeDeleted is the leaf Node
  remove the node
Else swap nodeDeleted with the lastNode
  remove nodeDeleted
   
minHeapify the array
'''

def max_heapify(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest)

def min_heapify(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] < A[k]:
        smallest = l
    else:
        smallest = k
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        min_heapify(A, smallest)

def left(k):
    return 2 * k + 1

def right(k):
    return 2 * k + 2

def build_max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(A,k)

def build_min_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        min_heapify(A,k)
        
A = [3,9,2,1,4,5]
build_max_heap(A)
print(A)
build_min_heap(A)
print(A)