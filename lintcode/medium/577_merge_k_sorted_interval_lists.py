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

        
# My own solution, using recursive merging. Time complexity is O(nlogk), where n is the total number of intervals.
Interval.__lt__ = lambda x, y: (x.start < y.start or (x.start == y.start and x.end < y.end))
class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        k = len(intervals)
        return self.merge_interval_lists(intervals, 0, k - 1)

    def merge_interval_lists(self, intervals, start, end):
        if start == end:
            return intervals[start]
        mid = (start + end) // 2
        left = self.merge_interval_lists(intervals, start, mid)
        right = self.merge_interval_lists(intervals, mid + 1, end)
        return self.merge_two_lists(left, right)

    def merge_two_lists(self, list_1, list_2):
        res = []
        i = j = 0
        while i < len(list_1) and j < len(list_2):
            if list_1[i] < list_2[j]:
                interval = list_1[i]
                i += 1
            else:
                interval = list_2[j]
                j += 1
            self.add_interval_to_list(res, interval)

        for ind_1 in range(i, len(list_1)):
            self.add_interval_to_list(res, list_1[ind_1])
        for ind_2 in range(j, len(list_2)):
            self.add_interval_to_list(res, list_2[ind_2])
        return res            
    
    def add_interval_to_list(self, res, interval):
        if not res:
            res.append(interval)
            return
        if interval.start > res[-1].end:
            res.append(interval)
            return
        res[-1].end = max(res[-1].end, interval.end)        

        
        
