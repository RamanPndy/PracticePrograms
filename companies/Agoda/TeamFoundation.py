'''
Problem statement
You are given two arrays, lowerSkill and higherSkill, representing developers arranged in increasing order of their skill levels.

For every developer i:
- lowerSkill[i] represents the maximum number of teammates they can accept who have less skill than them.
- higherSkill[i] represents the maximum number of teammates they can accept who have more skill than them.
Your task is to select the largest possible team such that every selected developer satisfies both conditions:
1. The number of selected teammates with lower skill must not exceed their lowerSkill[i].
2. The number of selected teammates with higher skill must not exceed their higherSkill[i].
Return the maximum possible team size.

Important: The selected developers do not need to be consecutive in the original arrays.
Example
Input:
lowerSkill = [0, 1, 1, 2]
higherSkill = [2, 1, 1, 0]

Output:
3

Explanation:
- Developer 0 can accept 0 lower-skilled and 2 higher-skilled teammates.
- Developer 1 can accept 1 lower-skilled and 1 higher-skilled teammates.
- Developer 2 can accept 1 lower-skilled and 1 higher-skilled teammates.
- Developer 3 can accept 2 lower-skilled and 0 higher-skilled teammates.
The largest possible team satisfying all conditions is [0, 1, 3] with size 3.

Input:
lowerSkill  = [1, 3, 2, 2, 2]
higherSkill = [2, 2, 1, 1, 3]

Output:
3

Explanation:
- Developer 0 can accept 1 lower-skilled and 2 higher-skilled teammates.
- Developer 1 can accept 3 lower-skilled and 2 higher-skilled teammates.
- Developer 2 can accept 2 lower-skilled and 1 higher-skilled teammates.
- Developer 3 can accept 2 lower-skilled and 1 higher-skilled teammates.
- Developer 4 can accept 2 lower-skilled and 3 higher-skilled teammates.
The largest possible team satisfying all conditions is [0, 1, 3] with size 3.

Key observation
Suppose we want to form a team of size k.

Since developers are already sorted by increasing skill, the selected developers will also be in increasing skill order.

For a selected developer at position j in the team (0-indexed):
- Number of lower-skilled teammates = j.
- Number of higher-skilled teammates = k - 1 - j.
Therefore, developer i can occupy position j only if:
\[
lowerSkill[i] \geq j
\]

and
\[
higherSkill[i] \geq k-1-j
\]

This gives us a straightforward way to check whether a team of size k is possible.

To find the maximum team size, we can perform a binary search on k from 1 to n (where n is the number of developers) and check for each k if a valid team can be formed using the above conditions. The largest k for which a valid team exists will be the answer.

Approach:
1. Define a helper function `can_form_team(k)` that checks if a team of size k can be formed.
2. In `can_form_team(k)`, try to assign each developer to a position j in the team such that `lowerSkill[i] >= j` and 
`higherSkill[i] >= k-1-j`.
3. If all positions from 0 to k-1 can be filled with valid developers, return True; otherwise, return False.
4. Perform a binary search on k from 1 to n to find the maximum team size for which `can_form_team(k)` returns True.
5. Return the maximum team size found.

why this works
----------------
The approach works because we are essentially trying to place developers in positions within the team such that their 
lowerSkill and higherSkill constraints are satisfied.
By checking each position j for a team of size k, we ensure that each developer can accommodate the required number
of lower-skilled and higher-skilled teammates.
Binary search helps us efficiently find the maximum team size by leveraging the monotonic property: if a team of size k 
is possible, then any team of size less than k is also possible.

Time Complexity:
O(n \log n) due to the binary search on team size and checking each team formation.
Space Complexity:
O(n) for storing the developers and any auxiliary data structures used in `can_form_team`.
'''
def max_team_size(lowerSkill, higherSkill):
    n = len(lowerSkill)

    def can_form_team(k):
        positions = list(range(k))
        for i in range(n):
            for j in range(len(positions)):
                if lowerSkill[i] >= positions[j] and higherSkill[i] >= k - 1 - positions[j]:
                    positions.pop(j)
                    break
        return not positions

    left, right = 1, n
    max_size = 0
    while left <= right:
        mid = (left + right) // 2
        if can_form_team(mid):
            max_size = mid
            left = mid + 1
        else:
            right = mid - 1
    return max_size