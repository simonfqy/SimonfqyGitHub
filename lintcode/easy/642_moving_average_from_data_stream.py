'''
Link: https://www.lintcode.com/problem/642/
'''

# My own solution. Simple, using Python deque. The optimization of keeping a local total_sum field ensures that the next()
# function has O(1) time complexity, no O(size).
from collections import deque
class MovingAverage(object):
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.size = size
        self.queue = deque([])
        self.total_sum = 0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        if len(self.queue) == self.size:
            val_popped = self.queue.popleft()
            self.total_sum -= val_popped
        self.queue.append(val)
        self.total_sum += val
        return self.total_sum / len(self.queue)
      
