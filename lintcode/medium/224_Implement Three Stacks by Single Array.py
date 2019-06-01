'''
Link: https://www.lintcode.com/problem/implement-three-stacks-by-single-array/description
'''

# My own solution after some painstaking debugging.
class ThreeStacks:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.stack_size = [0, 0, 0]
        self.array = []
        self.stack_count = 3

    """
    @param: stackNum: An integer
    @param: value: An integer
    @return: nothing
    """
    def push(self, stackNum, value):
        # Push value into stackNum stack
        ind_to_place = (self.stack_size[stackNum]) * self.stack_count + stackNum
        while ind_to_place > len(self.array) - 1:
            self.array.append(None)
        self.array[ind_to_place] = value     
        self.stack_size[stackNum] += 1

    """
    @param: stackNum: An integer
    @return: the top element
    """
    # The pop() function caused me a lot of headaches.
    def pop(self, stackNum):
        # Pop and return the top element from stackNum stack
        ind_to_pop = (self.stack_size[stackNum] - 1) * self.stack_count + stackNum
        if ind_to_pop < 0:
            return None
        element = self.array[ind_to_pop]
        trim_upper = True
        for val in self.array[ind_to_pop + 1:]:
            if val is not None:
                trim_upper = False
                self.array[ind_to_pop] = None
                break
        if trim_upper:
            while ind_to_pop <= len(self.array) - 1:
                self.array.pop()
        
        self.stack_size[stackNum] -= 1
        return element

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def peek(self, stackNum):
        # Return the top element
        size = self.stack_size[stackNum]
        if size <= 0:
            return None
        return self.array[(size - 1) * self.stack_count + stackNum]

    """
    @param: stackNum: An integer
    @return: true if the stack is empty else false
    """
    def isEmpty(self, stackNum):
        # write your code here
        return self.stack_size[stackNum] == 0
