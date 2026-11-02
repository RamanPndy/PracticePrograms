'''
Problem Statement
A computer has two CPU cores, Core 1 and Core 2, and a list of processes that must be considered in the given order.

A single latch determines which core makes the decision for each process. Initially, the latch belongs to Core 1.

For each process with execution time time[i], the core currently holding the latch has two choices:
1. Take the process
   - The current core processes the task and adds its execution time to its total.
   - The latch is passed to the other core.
2. Pass the process
   - The other core processes the task.
   - The current core keeps the latch for the next process.
Both cores act optimally to maximize their own final total execution time.

Return the final execution times of Core 1 and Core 2 as a two-element array.
Example
Input:
time = [10, 21, 10, 21, 10]

Output:
[41, 31]

Explanation
- Core 1 takes the first process (10), latch goes to Core 2.
- Core 2 takes the second process (21), latch goes to Core 1.
- Core 1 passes the third process (10) to Core 2, keeping the latch.
- Core 1 takes the fourth process (21), latch goes to Core 2.
- Core 2 takes the fifth process (10), latch goes to Core 1.
- Final execution times: Core 1 = 10 + 21 + 10 = 41, Core 2 = 21 + 10 = 31.

Key Insight
Instead of simulating both players with recursion, solve the game backwards.

Define:
- best = maximum total the current latch holder can guarantee from the remaining processes.
- suffix_sum = total execution time of the remaining suffix.
For each process (processing from right to left):
Option 1: Take
Current player gains the current task and hands over the latch.

Remaining total for current player becomes:
\(take = suffixSum - best\)Option 2: Pass
Current player keeps the latch.
\(pass = best\)Choose the better option:
\(best = \max(take, pass)\)

Approach:
Start from the last process and move backwards.
For each process, calculate the best total the current latch holder can guarantee.
Use the suffix sum to determine the remaining total for the current player if they take the process.
Compare the take and pass options to update the best total.
Continue until the first process to get the final execution times.

Why this works:
By solving the game backwards and using the suffix sum, we ensure that each core makes the optimal decision at each step,
considering the best possible outcome for the remaining processes. This guarantees that both cores maximize their own 
execution times while respecting the latch rules.

Example Walkthrough:
Consider the input time = [10, 21, 10, 21, 10].
- Start from the last process (10). Core 2 holds the latch and can either take it or pass it. Optimal choice is to take it.
- Move to the fourth process (21). Core 1 holds the latch and can either take it or pass it. Optimal choice is to take it.
- Move to the third process (10). Core 2 holds the latch and can either take it or pass it. Optimal choice is to pass it.
- Move to the second process (21). Core 1 holds the latch and can either take it or pass it. Optimal choice is to take it.
- Move to the first process (10). Core 2 holds the latch and can either take it or pass it. Optimal choice is to pass it.
- Final execution times: Core 1 = 41, Core 2 = 31.

Time Complexity:
O(n) due to memoization of the recursive states.
Space Complexity:
O(n) for the recursion stack and memoization cache.

Why does take = suffix_sum - best work?
Because best represents the maximum total the current latch holder can guarantee from the remaining processes. 
If the current player takes the current task, the remaining total for them is the total remaining execution time 
(suffix_sum) minus what the other player can guarantee (best). 
This ensures that the current player optimally maximizes their own execution time while considering the best possible 
outcome for the remaining processes.
'''

def maximize_sum_of_processed_times(time):
    best = 0
    suffix_sum = 0

    # Process from right to left
    for t in reversed(time):
        suffix_sum += t

        take = suffix_sum - best # If current player takes the task, remaining total for them is suffix_sum - best
        pass_option = best

        best = max(take, pass_option)

    first_core = best
    second_core = suffix_sum - best

    return [first_core, second_core]


# Example
print(maximize_sum_of_processed_times([10, 21, 10, 21, 10]))