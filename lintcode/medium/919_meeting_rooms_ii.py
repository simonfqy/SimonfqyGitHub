'''
Link: https://www.lintcode.com/problem/919/
'''

# My own solution. Uses heap.
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq
Interval.__lt__ = lambda x, y: x.start < y.start or (x.start == y.start and x.end < y.end)
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        intervals.sort()
        heap = []
        for interval in intervals:
            start_time, end_time = interval.start, interval.end
            if heap and heap[0] <= start_time:
                heapq.heappushpop(heap, end_time)
            else:
                heapq.heappush(heap, end_time)
        return len(heap)
      
      
# My implementation of a solution from a student on jiuzhang.com. Uses sweep line.
import bisect
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            bisect.insort(events, (interval.start, 1))
            bisect.insort(events, (interval.end, -1))
        max_count = 0
        concurrent_count = 0
        for _, delta in events:
            concurrent_count += delta
            max_count = max(max_count, concurrent_count)
        return max_count
    
    
    
