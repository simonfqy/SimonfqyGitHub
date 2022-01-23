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

   
# My own solution. Require that current_queue always only contain 1 element, such that every time top() operation only has O(1)
# time complexity, rather than the O(n) top() operation in the solution provided by jiuzhang.com.
from collections import deque
class Stack:
    def __init__(self):
        self.current_queue, self.majority_queue = deque(), deque()

    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        if self.current_queue:
            self.majority_queue.append(self.current_queue.popleft())
        self.current_queue.append(x)

    """
    @return: nothing
    """
    def pop(self):
        self.current_queue.popleft()
        while len(self.majority_queue) > 1:
            element = self.majority_queue.popleft()
            self.current_queue.append(element)
        self.current_queue, self.majority_queue = self.majority_queue, self.current_queue

    """
    @return: An integer
    """
    def top(self):
        return self.current_queue[0]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return (len(self.current_queue) + len(self.majority_queue)) == 0
    
    
# My own solution, which is slightly simplified from the solution on jiuzhang.com. Just like that one, the top() and pop() operations have O(n) 
# time complexity. The difference from the original solution is that, here we require that self.queue_1 contain the most recent element. So the 
# pointer swapping at the beginning of pop() and top() functions in the original solution is avoided here. 
from collections import deque
class Stack:
    def __init__(self):
        # queue_1 contains the most recent element.
        self.queue_1, self.queue_2 = deque(), deque()

    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        self.queue_1.append(x)

    """
    @return: nothing
    """
    def pop(self):
        while len(self.queue_1) > 1:
            self.queue_2.append(self.queue_1.popleft())
        self.queue_1.popleft()
        self.queue_1, self.queue_2 = self.queue_2, self.queue_1
        

    """
    @return: An integer
    """
    def top(self):
        while len(self.queue_1) > 1:
            self.queue_2.append(self.queue_1.popleft())
        return self.queue_1[0]
        

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return not self.queue_1
    
    
    
