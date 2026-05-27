Each node manages a range

Supports:

min/max/sum
range queries
lazy propagation
dynamic intervals

Core Idea

Tree where each node stores info about a range.
Example: [1,3,5,7]

Tree:
                 [1,3,5,7]
                   sum=16

               /            \
          [1,3]              [5,7]
           sum=4             sum=12

          /   \              /    \
        [1] [3]            [5]   [7]

Query Example
Range sum: sum(1..3)
Instead of scanning entire array: traverse only relevant nodes

Complexity:
Time: O(log N)

Use when:
complex range queries
min/max/gcd
many updates
lazy propagation