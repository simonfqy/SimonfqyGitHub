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
