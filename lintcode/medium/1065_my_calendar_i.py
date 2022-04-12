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
      
   
# My implementation of the search tree solution from jiuzhang.com. book() function has O(logn) time complexity on average
# and O(n) time complexity in the worst case.
class Node:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
    
    def insert(self, node):
        if node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        return False


class MyCalendar:

    def __init__(self):
        self.root = None        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """        
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))  
