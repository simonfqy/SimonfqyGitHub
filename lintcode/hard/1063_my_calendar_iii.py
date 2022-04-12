'''
Link: https://www.lintcode.com/problem/1063
'''

# My own solution. Also uses binary search and sweep line, just like question 1064.
import bisect
class MyCalendarThree:

    def __init__(self):
        self.events = []
        self.max_count = 0

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        start_event = (start, 1)
        end_event = (end, -1)
        bisect.insort(self.events, start_event)
        bisect.insort(self.events, end_event)
        concurrent_count = 0
        for time, delta in self.events:
            if time >= end:
                break
            concurrent_count += delta
            if concurrent_count > self.max_count:
                self.max_count = concurrent_count
        
        return self.max_count
      
      
      
