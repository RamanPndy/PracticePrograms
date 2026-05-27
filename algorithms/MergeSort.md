Merge sort is a Divide and Conquer algorithm

Idea:
Split array into halves
Sort each half recursively
Merge sorted halves

Complexity:
Time: O(N log N)
Space: O(N)

Because:
log N levels of recursion
each level processes all N elements

Height of recursion tree: log N
At every level total merge work: N
Total: N log N

Where Merge Sort Is Used
sorting
inversion count
count smaller elements
external sorting
stable sorting
Merge Sort pattern is useful whenever a problem involves:comparing elements across left and right halves
especially for:
inversion counting
smaller/greater element counting
sorting while preserving relationships

Core Merge Sort Pattern
During merge: Left half elements originally appeared BEFORE right half elements

Pattern Recognition
Problem involves pairs : (i,j)
Condition depends on ordering: nums[i] > nums[j]
need efficient counting:
Brute Force: O(N²)
Merge sort Counting: O(N log N)

IMPORTANT INTERVIEW RECOGNITION
Think merge-sort pattern when you see:
count pairs
count inversions
count smaller/greater elements
range pair conditions
order-sensitive counting
brute force O(N²)

| Signal                        | Meaning                    |
| ----------------------------- | -------------------------- |
| Count pairs                   | likely merge-sort counting |
| i < j conditions              | order-sensitive            |
| smaller/greater on left/right | inversion family           |
| brute force nested loops      | optimize using sorting     |
| pair inequalities             | sorted halves help         |
| O(N²) too slow                | think divide & conquer     |
| counting while sorting        | merge-sort pattern         |

MASTER INTERVIEW TRICK
If brute force looks like:
for i in range(n):
    for j in range(i+1, n):
Ask: Can sorted halves help me count faster?
if YES: merge sort pattern

Example:
[5,2,6,1]

Divide Phase
                [5,2,6,1]
               /         \
           [5,2]         [6,1]
           /   \         /   \
         [5]  [2]     [6]  [1]

Merge Phase
Merge upward:
[5] + [2] -> [2,5]

[6] + [1] -> [1,6]
Final:
[2,5] + [1,6]

Process:
1 < 2 -> take 1
2 < 6 -> take 2
5 < 6 -> take 5
take 6

Result:
[1,2,5,6]