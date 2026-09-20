# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
# determine if a person could attend all meetings.

# Example 1:
# Input: [[0,30],[5,10],[15,20]]
# Output: false

# Example 2:
# Input: [[7,10],[2,4]]
# Output: true

class Solution:
  '''
  Steps:
  1. sort all intervals
  2. traverse intervals from first index:
    - if current interval end > previous interval start then return false
  3. return true

  Question: Can a person attend all meetings without any overlaps?
  Approach:
  - Sort the intervals by their start times.
  - Traverse the sorted intervals and check if any interval overlaps with the previous one.
  - If an overlap is found, return False.
  - If no overlaps are found, return True.
  Time Complexity: O(n log n) due to sorting the intervals.
  Space Complexity: O(1) as we are using only a constant amount of extra space.
  Example:
  - Input: [[0,30],[5,10],[15,20]]
  - Output: False
  - Input: [[7,10],[2,4]]
  - Output: True
  Explanation:
  - In the first example, the meetings [0,30] and [5,10] overlap, so a person cannot attend all meetings.
  - In the second example, there are no overlapping meetings, so a person can attend all meetings.
  - The key idea is to first sort the intervals by their start times and then check for any overlaps between consecutive intervals.
  - This approach ensures that we efficiently check for overlaps with minimal additional space usage.
  - Overall, this method provides a clear and concise way to determine if all meetings can be attended without conflicts.
  '''
  def canAttendMeetings(self, intervals):
    intervals.sort()

    for i in range(1, len(intervals)):
      if intervals[i - 1][1] > intervals[i][0]:
        return False

    return True

