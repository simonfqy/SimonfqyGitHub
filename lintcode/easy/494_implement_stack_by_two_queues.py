'''
Link: https://www.lintcode.com/problem/implement-stack-by-two-queues/description
'''

# My own solution 2 months after reading the teachings on Jiuzhang.com.
from collections import deque
class Stack:
    def __init__(self):
        self.queue_1 = deque([])
        self.queue_2 = deque([])
        
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        if len(self.queue_2) > 0:
            the_queue = self.queue_2
        else:
            the_queue = self.queue_1
        the_queue.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        if len(self.queue_1) > 0:
            original_queue = self.queue_1
            new_queue = self.queue_2
        elif len(self.queue_2) > 0:
            original_queue = self.queue_2
            new_queue = self.queue_1
        else:
            return
        while len(original_queue) > 1:
            element = original_queue.popleft()
            new_queue.append(element)
        original_queue.popleft()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if len(self.queue_1) > 0:
            original_queue = self.queue_1
            new_queue = self.queue_2
        elif len(self.queue_2) > 0:
            original_queue = self.queue_2
            new_queue = self.queue_1
        else:
            return
        while original_queue:
            element = original_queue.popleft()
            new_queue.append(element)
        return element

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return len(self.queue_1) == 0 and len(self.queue_2) == 0
