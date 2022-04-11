'''
Link: https://www.lintcode.com/problem/1065/
'''

# My own solution. Rather dumb, uses straightforward list and tuple to do the job. book() function
# has O(nlogn) time complexity.
class MyCalendar:

    def __init__(self):
        self.booked_events = []        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """        
        for event_start, event_end in self.booked_events:
            if event_end <= start:
                continue
            if event_start >= end:
                break
            # Now we have event_end > start and event_start < end
            return False
        self.booked_events.append((start, end))
        self.booked_events.sort()
        return True
      
   
  
