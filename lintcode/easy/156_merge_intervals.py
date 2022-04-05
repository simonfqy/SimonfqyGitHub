'''
Link: https://www.lintcode.com/problem/merge-intervals/description

'''

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# This solution and the next one are provided by @Tin from jiuzhang.com. The problem is fairly similar to 
# https://www.lintcode.com/problem/insert-interval/description.
class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        answer = []
        intervals.sort(key = lambda x: x.start)
        last = None
        for interval in intervals:
            if last is None or interval.start > last.end:
                last = interval
                answer.append(last)
            else:
                last.end = max(last.end, interval.end)
        return answer
        
      
# Using two pointers.      
class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        if intervals is None or len(intervals) <= 1:
            return intervals
        intervals.sort(key = lambda x: x.start)
        # All elements up to the index left are correct ones with proper alignment.
        left, right = 0, 1
        while right < len(intervals):
            if intervals[left].end < intervals[right].start:
                left += 1
                # Copy the element pointed to by the right pointer to the element pointed to by the now-incremented
                # left pointer, and all elements now up to the new left pointer are legit intervals.
                intervals[left] = intervals[right]
                right += 1
            else:
                intervals[left].end = max(intervals[left].end, intervals[right].end)
                right += 1
        return intervals[:left + 1]     
    
    
# My own solution.
class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x.start)
        left, right = 0, 0
        results = []
        while right < len(intervals):
            start = intervals[left].start
            end = intervals[left].end
            while right < len(intervals) and intervals[right].start <= end:
                end = max(end, intervals[right].end)
                right += 1
            results.append(Interval(start, end))
            left = right
        return results
    
    
