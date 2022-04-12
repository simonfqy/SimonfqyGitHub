'''
Link: https://www.lintcode.com/problem/920
'''

# My own solution. Uses sort.
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

Interval.__lt__ = lambda x, y: x.start < y.start or (x.start == y.start and x.end < y.end)
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        last_time = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < last_time:
                return False
            last_time = max(last_time, interval.end)
        return True
      
      
      
