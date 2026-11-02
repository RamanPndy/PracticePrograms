'''
Question— Minimum capacity to finish chapters within D days
Problem: A printer processes chapters in order. Each chapter has a given number of pages, and chapters cannot be split across days. Find the minimum daily capacity needed to finish all chapters within D days.

Example:
Input: chapters = [100, 200, 300, 400], D = 2
Output: 600
Explanation: The minimum daily capacity to finish all chapters in 2 days is 600. One possible schedule is [100, 200, 300] on the first day and [400] on the second day.

Input: chapters = [100, 200, 300, 400], D = 3
Output: 400
Explanation: The minimum daily capacity to finish all chapters in 3 days is 400. One possible schedule is [100, 200] on the first day, [300] on the second day, and [400] on the third day.

Approach: Use binary search to find the minimum daily capacity.
1. Set the lower bound as the maximum number of pages in a single chapter.
2. Set the upper bound as the sum of all pages.
3. Perform binary search between the lower and upper bounds to find the minimum capacity that allows 
finishing all chapters within D days.

Why this works ?
The algorithm works by using binary search to efficiently narrow down the range of possible daily capacities. 
By checking if a given capacity can finish all chapters within D days, we can adjust the search range until 
we find the minimum feasible capacity.
Minimum possible capacity = largest chapter.
Maximum possible capacity = sum of all pages.
For a candidate capacity, greedily calculate how many days are required.
Reduce the search range when the capacity is sufficient.

Why does binary search work?
Binary search works because the problem exhibits a monotonic property: 
if a certain capacity can finish all chapters within D days, any larger capacity will also work. 
Conversely, if a capacity is insufficient, any smaller capacity will also be insufficient. 
This allows us to efficiently narrow down the search range to find the minimum feasible capacity.

What if chapters can be split?
If chapters can be split across days, the problem becomes simpler. 
The minimum daily capacity would then be the total number of pages divided by D, rounded up to the nearest integer. 
This is because we can distribute the pages evenly across the days.

What if the chapters must remain in order?
The current problem already assumes that chapters must remain in order. 
The binary search approach works under this constraint, as it checks if a given capacity can accommodate the chapters 
sequentially within D days.

Time Complexity: O(n * log(sum(chapters) - max(chapters))), where n is the number of chapters.
Space Complexity: O(1) (constant extra space)
'''

def min_capacity_to_finish_chapters(chapters, D):
    def can_finish(capacity):
        days = 1
        current_sum = 0
        for pages in chapters:
            if current_sum + pages > capacity:
                days += 1
                current_sum = 0
            current_sum += pages
        return days <= D

    low = max(chapters)
    high = sum(chapters)
    while low < high:
        mid = (low + high) // 2
        if can_finish(mid):
            high = mid
        else:
            low = mid + 1
    return low

# Example usage:
chapters = [100, 200, 300, 400]
D = 2
print(min_capacity_to_finish_chapters(chapters, D))  # Output: 600

chapters = [100, 200, 300, 400]
D = 3
print(min_capacity_to_finish_chapters(chapters, D))  # Output: 400