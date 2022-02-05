'''
Link: https://www.lintcode.com/problem/577/
'''

# My own solution. Uses heap to order the intervals, and always compare the interval to be added against the last interval in the result list.
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq
Interval.__lt__ = lambda x, y: (x.start < y.start or (x.start == y.start and x.end < y.end))
class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        min_heap = []
        for i, interval_list in enumerate(intervals):
            if not interval_list:
                continue
            heapq.heappush(min_heap, (interval_list[0], i, 0))
        res = []
        while min_heap:
            interval, list_ind, ind_in_list = heapq.heappop(min_heap)
            self.add_interval_to_list(res, interval)
            ind_in_list += 1            
            if len(intervals[list_ind]) > ind_in_list:
                heapq.heappush(min_heap, (intervals[list_ind][ind_in_list], list_ind, ind_in_list))
        return res


    def add_interval_to_list(self, res, interval):
        if not res:
            res.append(interval)
            return
        if interval.start > res[-1].end:
            res.append(interval)
            return
        res[-1].end = max(res[-1].end, interval.end)

        
        
