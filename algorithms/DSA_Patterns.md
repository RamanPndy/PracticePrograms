When should you think about:
1. Merge Sort counting
2. Fenwick Tree
3. Segment Tree

Usually when problem says:
1. count smaller/greater elements
2. on left/right side
3. dynamic frequencies
4. range queries
5. inversion counting

<h2>Greedy Algorithm</h2>
Greedy is one of the most important algorithmic thinking patterns.

The core idea is:

> “At every step, make the best immediate/local choice.”

without worrying too much about the future.

---

# Simple Real-Life Example

Suppose you have currency notes:

```text id="8dmsku"
₹500, ₹200, ₹100, ₹50, ₹20, ₹10
```

Need:

```text id="ww7gq1"
₹880
```

Greedy approach says:

```text id="u4os3t"
Take biggest possible note first
```

Process:

```text id="jlwm9p"
500 → remaining 380
200 → remaining 180
100 → remaining 80
50  → remaining 30
20  → remaining 10
10  → remaining 0
```

Done.

This works because:

```text id="w1r75w"
largest choice helps optimally
```

---

# Formal Meaning Of Greedy

A greedy algorithm:

1. Builds answer step-by-step
2. Chooses locally optimal option
3. Never revisits decisions

---

# Important Characteristic

Greedy says:

```text id="r3e5t0"
"Best choice NOW
will eventually lead to global best solution."
```

That’s the key assumption.

---

# Your Squares Example

Problem:

```text id="jlwm6v"
x = 41
```

Greedy thinking:

```text id="jlwm7a"
Take largest square possible first
```

Largest square:

```text id="jlwm4z"
6² = 36
```

Remaining:

```text id="jlwm3d"
5
```

Again:

```text id="jlwm8c"
largest square <= 5
→ 2² = 4
```

Remaining:

```text id="jlwm0m"
1
```

Answer:

```text id="jlwm1u"
[6,2,1]
```

---

# Why Called "Greedy"?

Because algorithm behaves like:

```text id="jlwm7k"
"Give me the biggest/best thing immediately."
```

It does not carefully explore all possibilities.

---

# IMPORTANT:

Greedy Does NOT Always Work

Example:

Coin system:

```text id="jlwm8i"
coins = [1,3,4]
target = 6
```

Greedy:

```text id="8o5b8q"
take 4
remaining 2

take 1
take 1

Total = 3 coins
```

But optimal:

```text id="jlwm9b"
3 + 3
```

Only:

```text id="jlwm7z"
2 coins
```

So greedy failed.

---

# BIG QUESTION

# How To Recognize Greedy Problems?

This is the real interview skill.

---

# SIGNALS OF GREEDY

---

# 1. Problem asks for:

* minimum
* maximum
* smallest
* largest
* earliest
* latest

Example:

```text id="jlwm6l"
minimum intervals
maximum profit
```

---

# 2. Local Best Choice Seems Natural

Example:

```text id="74v2pd"
always pick earliest finishing meeting
```

---

# 3. Once Decision Taken, Never Reconsidered

Greedy rarely backtracks.

---

# 4. Sorting Helps A Lot

Many greedy problems begin with:

```python id="yiy1r0"
sort(...)
```

Examples:

* interval scheduling
* activity selection
* job sequencing

---

# 5. Problem Has "Optimal Substructure"

Meaning:

```text id="u1lchz"
best overall solution
contains best smaller solutions
```

---

# 6. Brute Force Tries Many Combinations

But one obvious best move exists.

---

# HOW TO VERIFY GREEDY WORKS?

This is hardest part.

You usually need intuition/proof.

---

# Common Greedy Proof Idea

## Exchange Argument

Show:

```text id="jlwm9m"
If optimal solution didn't take greedy choice,
we can swap choices and still remain optimal.
```

---

# Example: Activity Selection

Choose maximum non-overlapping meetings.

Greedy:

```text id="jlwm7h"
pick meeting that finishes earliest
```

Why correct?

Because:

```text id="8qgdb9"
finishing earlier leaves maximum room for future meetings
```

---

# MOST COMMON GREEDY PATTERNS

---

# 1. Interval Problems

Keywords:

```text id="jlwm4q"
meeting
interval
schedule
overlap
```

Usually:

* sort by end time
* greedy pick

---

# 2. Largest/Smallest Construction

Examples:

* largest number
* minimum cost
* smallest lexicographic string

---

# 3. Resource Allocation

Examples:

* assign jobs
* distribute candies
* gas station

---

# 4. Huffman Encoding

Always combine:

```text id="qhub5u"
two smallest
```

Greedy.

---

# 5. Jump Problems

Example:
Jump Game

Greedy:

```text id="5jlwm"
track farthest reachable index
```

---

# 6. Stock Problems

Sometimes:

```text id="rjlwm"
buy low sell high greedily
```

---

# WHEN GREEDY USUALLY FAILS

If problem requires:

* trying combinations
* revisiting decisions
* future choices matter heavily

Then likely:

* DP
* backtracking
* graph search

needed.

---

# DIFFERENCE BETWEEN GREEDY VS DP

## Greedy

```text id="djlwm"
take best immediate choice
```

Fast:

```text id="pjlwm"
usually O(N log N)
```

No reconsideration.

---

## Dynamic Programming

```text id="3jlwm"
explore multiple possibilities carefully
```

Stores best results.

---

# EASY COMPARISON

## Greedy

Like climbing mountain by:

```text id="9jlwm"
always taking steepest upward step
```

---

## DP

Like checking:

```text id="4jlwm"
many possible paths before deciding
```

---

# INTERVIEW RECOGNITION CHEAT SHEET

Think GREEDY when you see:

| Signal               | Possible Greedy |
| -------------------- | --------------- |
| intervals            | yes             |
| scheduling           | yes             |
| minimum removals     | yes             |
| maximize count       | yes             |
| local best obvious   | yes             |
| sorting helpful      | yes             |
| no revisiting needed | yes             |

---

# GOLDEN QUESTION TO ASK YOURSELF

While solving:

```text id="xjlwm"
"If I make the best choice right now,
can it ever hurt future choices?"
```

If answer seems:

```text id="yjlwm"
"No"
```

then greedy may work.

<h2>Dynamic Programming</h2>
Dynamic Programming (DP) is fundamentally about:

> Solving overlapping smaller subproblems and reusing their answers.

The biggest challenge is not writing DP code.

It is:

```text id="jlwmdp1"
recognizing that a problem IS DP
```

---

# CORE IDEA OF DP

DP is useful when:

```text id="jlwmdp2"
same subproblems repeat again and again
```

and brute force becomes exponential.

---

# Simple Fibonacci Example

Recursive Fibonacci:

```python id="f4j3k0"
def fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)
```

Problem:

```text id="jlwmdp3"
fib(3)
fib(2)
fib(3)
fib(2)
```

recomputed many times.

DP stores answers:

```text id="jlwmdp4"
memoization
```

so each solved once.

---

# MOST IMPORTANT DP RECOGNITION SIGNALS

---

# 1. Problem asks:

* count ways
* minimum cost
* maximum profit
* optimal strategy
* longest
* shortest
* possible or not

Examples:

```text id="jlwmdp5"
minimum coins
maximum path
longest subsequence
```

Huge DP signal.

---

# 2. Brute Force Tries ALL Possibilities

Example:

```text id="jlwmdp6"
take or not take
```

If recursion tree explodes:

```text id="jlwmdp7"
2^N
```

DP likely.

---

# 3. Choices At Every Step

Example:

```text id="jlwmdp8"
at index i:
- pick current
- skip current
```

Very strong DP indicator.

---

# 4. Same State Appears Again

Suppose:

```text id="jlwmdp9"
solve(index=5, sum=10)
```

reached from multiple paths.

That means:

```text id="jlwmdp10"
overlapping subproblems
```

→ DP.

---

# 5. Future Depends On Current Decision

Unlike greedy:

```text id="jlwmdp11"
current choice affects future heavily
```

So need careful exploration.

---

# MOST IMPORTANT DP QUESTION

Ask yourself:

```text id="jlwmdp12"
"Can problem be described using smaller versions of itself?"
```

If YES:

* recursion likely
* memoization likely
* DP likely

---

# CLASSIC DP PATTERNS

---

# 1. Take / Not Take DP

Most common.

Example:

* subset sum
* knapsack
* partition

At each index:

```text id="jlwmdp13"
Take nums[i]
OR
Skip nums[i]
```

---

# Example Problem

## Subset Sum

Can we form target?

```text id="jlwmdp14"
nums = [1,2,3]
target = 5
```

Choices:

```text id="jlwmdp15"
take 2
skip 2
```

Repeated recursively.

DP stores states.

---

# 2. Linear DP

State depends on previous positions.

Examples:

* climbing stairs
* house robber
* fibonacci

---

# Example: Climbing Stairs

```text id="jlwmdp16"
ways(n) = ways(n-1) + ways(n-2)
```

because:

* last jump 1-step
* or 2-step

---

# 3. Interval DP

DP on ranges.

Examples:

* matrix chain multiplication
* burst balloons
* palindrome partitioning

State:

```text id="jlwmdp17"
dp[l][r]
```

---

# 4. String DP

Huge category.

Examples:

* longest common subsequence
* edit distance
* palindrome subsequence

State often:

```text id="jlwmdp18"
dp[i][j]
```

---

# 5. Grid DP

Move in matrix.

Examples:

* unique paths
* minimum path sum

State:

```text id="jlwmdp19"
dp[row][col]
```

---

# 6. Decision-Making Games

Examples:

* stone game
* optimal play problems

Usually:

```text id="jlwmdp20"
minimax + DP
```

---

# HOW TO THINK IN DP

---

# Step 1: Define State

Most important step.

Ask:

```text id="jlwmdp21"
"What uniquely defines a subproblem?"
```

Examples:

```text id="jlwmdp22"
index
index + remaining_sum
left + right
```

---

# Step 2: Define Choices

At state:

```text id="jlwmdp23"
what decisions are possible?
```

---

# Step 3: Recurrence Relation

How smaller answers combine.

Example:

```text id="jlwmdp24"
dp[i] = min(
    take,
    skip
)
```

---

# Step 4: Memoize

Store repeated states.

---

# HUGE INTERVIEW RECOGNITION TRICK

If brute force recursion looks like:

```python id="jlwmdp25"
def solve(i, something):
```

AND:

```text id="jlwmdp26"
same parameters repeat
```

then:

```text id="jlwmdp27"
convert to DP
```

---

# GREEDY VS DP

This is critical.

---

# Greedy

```text id="jlwmdp28"
Best immediate choice
```

No revisiting.

---

# DP

```text id="jlwmdp29"
Explore multiple choices carefully
```

because local best may fail.

---

# Example

Coins:

```text id="jlwmdp30"
[1,3,4]
target=6
```

Greedy:

```text id="jlwmdp31"
4+1+1 = 3 coins
```

Optimal:

```text id="jlwmdp32"
3+3 = 2 coins
```

Need DP.

---

# COMMON DP INTERVIEW SIGNALS

| Signal                | Likely DP |
| --------------------- | --------- |
| count ways            | YES       |
| minimum operations    | YES       |
| maximum profit        | YES       |
| subsequence           | YES       |
| partition             | YES       |
| choose or skip        | YES       |
| recursive brute force | YES       |
| overlapping states    | YES       |
| optimization problem  | YES       |

---

# WHEN DP IS VERY LIKELY

If constraints:

```text id="jlwmdp33"
N = 10^2
10^3
10^4
```

and brute force:

```text id="jlwmdp34"
2^N
```

obviously impossible.

Then interviewer expects:

```text id="jlwmdp35"
DP optimization
```

---

# MASTER MENTAL MODEL

DP is basically:

```text id="jlwmdp36"
Brute force recursion
+
Caching repeated work
```

That’s the simplest way to understand it.

---

# GOLDEN QUESTION

Ask yourself:

```text id="jlwmdp37"
"Am I solving the same smaller problem repeatedly?"
```

If YES:

```text id="jlwmdp38"
DP candidate
```

---

# EASY RECOGNITION FLOW

## Problem has:

* choices?
* optimization?
* counting?
* recursion?
* repeated states?

Then think:

```text id="jlwmdp39"
DP
```

---

# MOST IMPORTANT SKILL

Do NOT memorize DP solutions.

Instead train yourself to identify:

```text id="jlwmdp40"
State
Choices
Transition
```

That is real DP mastery.

This is the real turning point in learning DP.

Most people try to memorize:

* knapsack DP
* LIS DP
* grid DP

But strong DP intuition comes from understanding:

> “What information must I remember to solve future problems?”

That remembered information becomes your DP state.

---

# THE MOST IMPORTANT DP IDEA

DP table is NOT random.

It represents:

```text id="dpintu1"
all unique subproblems
```

So first ask:

```text id="dpintu2"
"What defines a subproblem?"
```

That determines:

* 1D DP
* 2D DP
* 3D DP

---

# STEP-BY-STEP DP THINKING PROCESS

Always think in this order:

---

# STEP 1: Write Brute Force Recursion

Before DP:

* do recursion first
* identify choices

Because DP is just:

```text id="dpintu3"
cached recursion
```

---

# Example 1: Climbing Stairs

Problem:

```text id="dpintu4"
You can climb 1 or 2 steps.
How many ways to reach n?
```

---

# Recursive Thinking

At stair:

```text id="dpintu5"
i
```

choices:

```text id="dpintu6"
jump 1
jump 2
```

Recurrence:

```text id="dpintu7"
ways(i) =
ways(i+1) + ways(i+2)
```

---

# What Defines Subproblem?

Only:

```text id="dpintu8"
current stair index
```

So ONE variable changes.

Therefore:

```text id="dpintu9"
1D DP
```

Use:

```text id="dpintu10"
dp[i]
```

---

# HUGE RULE

# Number of changing variables

≈

# DP dimensions

This is one of most important DP intuitions.

---

# Example 2: Grid Paths

Problem:

```text id="dpintu11"
Count paths from top-left to bottom-right.
```

---

# Recursive State

To define current subproblem, need:

```text id="dpintu12"
row
col
```

Two changing variables.

Therefore:

```text id="dpintu13"
2D DP
```

Use:

```text id="dpintu14"
dp[row][col]
```

---

# Example 3: Knapsack

Problem:

```text id="dpintu15"
Choose items maximizing value within capacity.
```

---

# What Defines State?

Need:

```text id="dpintu16"
current index
remaining capacity
```

Two variables changing.

Therefore:

```text id="dpintu17"
2D DP
```

Use:

```text id="dpintu18"
dp[i][capacity]
```

---

# Example 4: Longest Common Subsequence

Need:

```text id="dpintu19"
position in string1
position in string2
```

Two changing indices.

Therefore:

```text id="dpintu20"
2D DP
```

---

# THE BIGGEST DP SECRET

Most DP problems are:

```text id="dpintu21"
"What minimum information must I remember?"
```

That becomes state.

---

# HOW TO IDENTIFY 1D VS 2D DP

---

# 1D DP

Use when problem progression depends on:

* one index
* one variable

Examples:

* Fibonacci
* House Robber
* Climbing Stairs
* LIS

State:

```text id="dpintu22"
dp[i]
```

---

# 2D DP

Use when state depends on:

* two changing things

Examples:

* grids
* two strings
* index + capacity
* interval ranges

State:

```text id="dpintu23"
dp[i][j]
```

---

# 3D DP

Rare.

Use when:

* three variables change

Example:

```text id="dpintu24"
dp[i][j][k]
```

Usually:

* index
* remaining sum
* operations left

---

# VERY IMPORTANT MENTAL MODEL

DP table is just:

```text id="dpintu25"
memoization storage
```

Nothing magical.

---

# Example: Fibonacci

Recursive:

```python id="fibdp1"
fib(n) = fib(n-1) + fib(n-2)
```

Memoization:

```python id="fibdp2"
dp[n]
```

because only variable:

```text id="dpintu26"
n
```

changes.

---

# HOW TO BUILD DP INTUITION

# Always Ask These 4 Questions

---

# 1. What are my choices?

Example:

```text id="dpintu27"
take / skip
left / right
up / down
```

---

# 2. What changes after choice?

Those changing values become DP state.

---

# 3. Can same state appear again?

If YES:

```text id="dpintu28"
DP needed
```

---

# 4. What minimum info uniquely identifies state?

That defines dimensions.

---

# GOLDEN EXAMPLES

---

# Example: House Robber

Problem:

```text id="dpintu29"
cannot rob adjacent houses
```

State:

```text id="dpintu30"
current index
```

Only one variable.

So:

```text id="dpintu31"
1D DP
```

---

# Example: Edit Distance

Need:

```text id="dpintu32"
position in word1
position in word2
```

Two variables.

So:

```text id="dpintu33"
2D DP
```

---

# Example: Burst Balloons

Need:

```text id="dpintu34"
left boundary
right boundary
```

Two changing range endpoints.

So:

```text id="dpintu35"
interval DP
```

---

# WHEN MATRIX IS CREATED

You create matrix DP when:

* state depends on TWO things simultaneously

Usually:

* two indices
* row/col
* index/capacity
* left/right boundaries

---

# EASY RECOGNITION TABLE

| Problem Type         | State      | DP Type |
| -------------------- | ---------- | ------- |
| linear progression   | i          | 1D      |
| grid traversal       | row,col    | 2D      |
| two strings          | i,j        | 2D      |
| knapsack             | i,capacity | 2D      |
| intervals            | l,r        | 2D      |
| multiple constraints | i,j,k      | 3D      |

---

# TOP-DOWN VS BOTTOM-UP

---

# Top-Down (Memoization)

Feels natural.

Write recursion first.

Store results.

---

# Bottom-Up (Tabulation)

Convert recursion dependencies into loops.

---

# IMPORTANT INTUITION

Top-down helps understand:

```text id="dpintu36"
state and transitions
```

Bottom-up helps optimize.

---

# MASTER DP INTUITION

DP is NOT about arrays/matrices.

DP is about:

```text id="dpintu37"
representing subproblems efficiently
```

The table is just storage.

---

# FINAL GOLDEN RULE

To determine DP dimensions:

Ask:

```text id="dpintu38"
"What variables change during recursion?"
```

Those variables define:

* DP state
* DP dimensions
* matrix size

That is the core intuition behind DP.

<h2>BackTracking</h2>
Backtracking is basically:

> “Try a choice → go deeper → if it fails, undo the choice and try another.”

It is DFS (Depth First Search) on possibilities.

---

# SIMPLE REAL-LIFE ANALOGY

Imagine maze solving.

At every junction:

* choose a path
* walk ahead
* if dead end:

  * come back
  * try another path

That “come back and try again” is:

```text id="bt1"
BACKTRACKING
```

---

# CORE IDEA

Backtracking explores:

```text id="bt2"
all possible choices
```

systematically.

---

# THE MOST IMPORTANT THING

Backtracking has 3 steps:

---

# 1. Choose

Take one option.

Example:

```text id="bt3"
pick number 2
```

---

# 2. Explore

Go deeper recursively.

---

# 3. Undo (Backtrack)

Remove previous choice.

Example:

```text id="bt4"
remove 2
```

Then try next possibility.

---

# SIMPLEST EXAMPLE

# Generate All Subsets

Input:

```text id="bt5"
[1,2]
```

Output:

```text id="bt6"
[]
[1]
[2]
[1,2]
```

---

# HOW HUMAN THINKS

At each number:

```text id="bt7"
take it
OR
skip it
```

---

# RECURSION TREE

```text id="bt8"
                 []
              /      \
           take1    skip1
            /          \
         [1]            []
        /   \          /   \
    [1,2]  [1]      [2]   []
```

Backtracking explores entire tree.

---

# CODE

```python id="bt9"
def subsets(nums):
    result = []

    def backtrack(index, path):

        result.append(path[:])

        for i in range(index, len(nums)):

            path.append(nums[i])      # choose

            backtrack(i+1, path)      # explore

            path.pop()                # undo

    backtrack(0, [])

    return result
```

---

# VISUAL EXECUTION

Start:

```text id="bt10"
path = []
```

Choose:

```text id="bt11"
1
```

Now:

```text id="bt12"
[1]
```

Choose:

```text id="bt13"
2
```

Now:

```text id="bt14"
[1,2]
```

No more choices.

Backtrack:

```text id="bt15"
remove 2
```

Back to:

```text id="bt16"
[1]
```

Backtrack again:

```text id="bt17"
remove 1
```

Back to:

```text id="bt18"
[]
```

Now try:

```text id="bt19"
2
```

---

# THAT IS BACKTRACKING

```text id="bt20"
make choice
go deeper
undo choice
try next
```

---

# WHY UNDO IS IMPORTANT

Without undo:

* previous choices pollute future paths

Example:

```text id="bt21"
path.append(1)
```

If we never remove:

```text id="bt22"
all future paths incorrectly contain 1
```

---

# ANOTHER EXAMPLE

# Permutations

Input:

```text id="bt23"
[1,2,3]
```

Output:

```text id="bt24"
[1,2,3]
[1,3,2]
[2,1,3]
...
```

---

# THINKING

At every position:

```text id="bt25"
which unused number can I place?
```

---

# TREE

```text id="bt26"
                []
          /       |       \
        1         2        3
      /  \      /  \     /  \
    2     3   1    3   1    2
```

---

# TEMPLATE OF BACKTRACKING

Most problems follow:

```python id="bt27"
def backtrack(state):

    if goal reached:
        save answer
        return

    for choice in choices:

        make choice

        backtrack(new state)

        undo choice
```

This template solves MOST backtracking problems.

---

# HOW TO IDENTIFY BACKTRACKING PROBLEMS

Usually asks:

* generate all
* all combinations
* all permutations
* all paths
* all arrangements
* possible configurations

---

# HUGE SIGNAL WORDS

| Problem Statement | Likely Backtracking |
| ----------------- | ------------------- |
| generate all      | YES                 |
| all subsets       | YES                 |
| permutations      | YES                 |
| sudoku            | YES                 |
| n-queens          | YES                 |
| word search       | YES                 |
| maze paths        | YES                 |
| combination sum   | YES                 |

---

# DIFFERENCE BETWEEN BACKTRACKING VS DP

---

# Backtracking

Explores ALL possibilities.

Goal:

```text id="bt28"
generate/search
```

Often exponential.

---

# DP

Avoids repeated work.

Goal:

```text id="bt29"
optimization/counting
```

Stores states.

---

# BACKTRACKING IS DFS ON DECISION TREE

This is the best mental model.

Every recursive call:

```text id="bt30"
one node in decision tree
```

Every choice:

```text id="bt31"
one branch
```

---

# CLASSIC BACKTRACKING PROBLEMS

---

# 1. Subsets

Choice:

```text id="bt32"
take / skip
```

---

# 2. Permutations

Choice:

```text id="bt33"
pick unused element
```

---

# 3. Combination Sum

Choice:

```text id="bt34"
pick number again or move ahead
```

---

# 4. N-Queens

Choice:

```text id="bt35"
where to place queen
```

---

# 5. Sudoku

Choice:

```text id="bt36"
which digit fits here
```

---

# MOST IMPORTANT INTUITION

Backtracking means:

```text id="bt37"
"Try possibilities one-by-one.
If path becomes invalid,
come back."
```

That’s all.

---

# GOLDEN RECOGNITION QUESTION

Ask:

```text id="bt38"
"Do I need to explore multiple possible choices?"
```

If YES:

* recursion tree exists
* backtracking likely

---

# SIMPLE VISUAL SUMMARY

```text id="bt39"
Choose
   ↓
Explore
   ↓
Undo
   ↓
Try next choice
```

This cycle repeats recursively.
