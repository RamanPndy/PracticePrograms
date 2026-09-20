# Medium
# Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), 
# find the minimum number of conference rooms required.
# Example 1:
# Input:
# [[0, 30],[5, 10],[15, 20]]
# Output:
#  2

import heapq
class Solution:
  # Time: O(sort)
  # Space: O(n)
  '''
  1. create variable to store total intervals
  2. create vars to store start and end of all intervals.
  3. traverse intervals array and add start and end of intervals in respective arrays.
  4. sort start and end intervals arrays
  5. create right pointer and set to 0.
  6. traverse total intervals by index
    - if starts[current index] < ends[right pointer] then increase answer
    - otherwise increase right pointer
  7. return answer

  Question: How can we determine the minimum number of conference rooms required for the given meeting intervals?
  Approach:
  - Separate the start and end times of all meetings.
  - Sort the start and end times.
  - Use two pointers to traverse the start and end times.
  - If a meeting starts before the earliest ending meeting ends, we need a new room.
  - Otherwise, we can reuse a room that has been freed.
  - Keep track of the maximum number of rooms needed at any time.
  Time Complexity: O(n log n) due to sorting the start and end times.
  Space Complexity: O(n) for storing the start and end times.
  Example:
  - Input: [[0, 30],[5, 10],[15, 20]]
  - Output: 2
  - Explanation: At time 0, one meeting starts, requiring one room. At time 5, another meeting starts while the first one is still ongoing, requiring a second room. At time 10, the second meeting ends, freeing up a room. At time 15, a new meeting starts, reusing the freed room. The maximum number of rooms needed at any time is 2.
  - At time 0, one meeting starts, requiring one room.
  - At time 5, another meeting starts while the first one is still ongoing, requiring a second room.
  - At time 10, the second meeting ends, freeing up a room.
  - At time 15, a new meeting starts, reusing the freed room.
  - The maximum number of rooms needed at any time is 2.
  '''
  def minMeetingRooms(self, intervals):
    n = len(intervals)
    ans = 0
    starts = []
    ends = []

    for start, end in intervals:
      starts.append(start)
      ends.append(end)

    starts.sort()
    ends.sort()

    j = 0
    for i in range(n):
      if starts[i] < ends[j]:
        ans += 1
      else:
        j += 1

    return ans

class Solution:
  # Time: O(sort)
  # Space: O(n)
  def minMeetingRooms(self, intervals):
    minHeap = []  # Store end times of each room.

    for start, end in sorted(intervals):
      # No overlap, we can reuse the same room.
      if minHeap and start >= minHeap[0]:
        heapq.heappop(minHeap)
      heapq.heappush(minHeap, end)

    return len(minHeap)
