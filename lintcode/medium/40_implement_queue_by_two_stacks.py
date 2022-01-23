'''
Link: https://www.lintcode.com/problem/implement-queue-by-two-stacks/description
'''

# Based on the teaching from jiuzhang.com. When I was thinking I thought of a brute-force solution,
# in which I thought that after each popping, the pop_stack should pop all its elements and push them into
# push_stack, but it turned out that this was not necessary, we would not have problems if we simply keep the
# remaining elements inside the pop_stack.
class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.push_stack = []
        self.pop_stack = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.push_stack.append(element)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if len(self.pop_stack) == 0:
            while self.push_stack:
                ele = self.push_stack.pop()
                self.pop_stack.append(ele)        
        return self.pop_stack.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if len(self.pop_stack) == 0:
            while self.push_stack:
                ele = self.push_stack.pop()
                self.pop_stack.append(ele)        
        return self.pop_stack[-1]

    
# My own solution. Push() has O(n) time complexity, while pop() and top() has O(1) time complexity.
# Stack_1 is the stack containing all the elements (in reverse order), while stack_2 shouldn't contain any element.
class MyQueue:
    
    def __init__(self):
        self.stack_1, self.stack_2 = [], []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        self.stack_1.append(element)
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())

    """
    @return: An integer
    """
    def pop(self):
        return self.stack_1.pop()

    """
    @return: An integer
    """
    def top(self):
        return self.stack_1[-1]
    
    
# Another of my own solution. push() has O(1) time complexity, while pop() and top() have O(n) time complexity. 
class MyQueue:
    
    def __init__(self):
        self.stack_1, self.stack_2 = [], []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        self.stack_1.append(element)

    """
    @return: An integer
    """
    def pop(self):
        while len(self.stack_1) > 1:
            self.stack_2.append(self.stack_1.pop())
        element = self.stack_1.pop()
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())
        return element

    """
    @return: An integer
    """
    def top(self):
        while len(self.stack_1) > 1:
            self.stack_2.append(self.stack_1.pop())
        element = self.stack_1[0]
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())
        return element
    
    
