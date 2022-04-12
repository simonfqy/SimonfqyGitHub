'''
Link: https://www.lintcode.com/problem/1064
'''

# My own solution. Uses binary search and sweep line algorithm to achieve the objective. Has O(n) time complexity
# for the book() function. 
import bisect
class MyCalendarTwo:

    def __init__(self):
        self.events = []        

    """
    @param start: 
    @param end: 
    @return: nothing
    """
    def book(self, start, end):
        updated_events = list(self.events)
        start_event = (start, 1)
        end_event = (end, -1)
        bisect.insort(updated_events, start_event)
        bisect.insort(updated_events, end_event)
        current_event_count = 0
        for time, delta in updated_events:
            if time >= end:
                break
            current_event_count += delta
            if current_event_count >= 3:
                return False
        self.events = updated_events
        return True
        

        
