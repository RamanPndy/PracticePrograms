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
  '''
  def canAttendMeetings(self, intervals):
    intervals.sort()

    for i in range(1, len(intervals)):
      if intervals[i - 1][1] > intervals[i][0]:
        return False

    return True

