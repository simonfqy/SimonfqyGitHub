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
    
    
# Solution from Jiuzhang.com. Quite complicated, but more suitable when the 3 stacks differ greatly in sizes.
'''
算法描述
这道题的本质是把数组索引当作地址，用链表来实现栈。数组buffer中的每一个元素，并不能单单是简单的int类型，而是一个链表中的节点，
它包含值value，栈中向栈底方向的之前元素索引prev，向栈顶方向的后来元素索引next。
在该三栈数据结构中，要记录三个栈顶指针stackPointer，也就是三个栈顶所在的数组索引，通过这三个栈顶节点，能够用prev找到整串栈。
此外还要用indexUsed记录整个数组中的所用的索引数。其实也就是下一次push的时候，向数组的indexUsed位置存储。

具体操作：

构造：要初始化stackPointer为3个-1,表示没有;indexUsed=0;buffer为一个长度为三倍栈大小的数组。
push：要把新结点new在buffer[indexUsed]，同时修改该栈的stackPointer，indexUsed自增。注意修改当前栈顶结点prev和之前栈顶结点的next索引。
peek：只需要返回buffer中对应的stackPointer即可。
isEmpty：只需判断stackPointer是否为-1。
pop：pop的操作较为复杂，因为有三个栈，所以栈顶不一定在数组尾端，pop掉栈顶之后，数组中可能存在空洞。而这个空洞又很难push入元素。所以，
解决方法是，当要pop的元素不在数组尾端（即indexUsed-1）时，交换这两个元素。不过一定要注意，交换的时候，要注意修改这两个元素之前、
之后结点的prev和next指针，使得链表仍然是正确的，事实上这就是结点中next的作用——为了找到之后结点并修改它的prev。在交换时，一种很特殊的
情况是栈顶节点刚好是数组尾端元素的后继节点，这时需要做特殊处理。在交换完成后，就可以删掉数组尾端元素，并修改相应的stackPointer、
indexUsed和新栈顶的next。
'''

class ThreeStacks:
    def __init__(self, size):
        self.stackSize = size
        self.stackPointer = [-1, -1, -1]
        self.indexUsed = 0
        self.buffer = [StackNode(-1, -1, -1) for _ in range(size*3)]

    def push(self, stackNum, value):
        lastIndex = self.stackPointer[stackNum]
        self.stackPointer[stackNum] = self.indexUsed
        self.indexUsed += 1
        self.buffer[self.stackPointer[stackNum]] = StackNode(lastIndex, value, -1)
        if lastIndex != -1:
            self.buffer[lastIndex].next = self.stackPointer[stackNum]

    def pop(self, stackNum):
        value = self.buffer[self.stackPointer[stackNum]].value
        lastIndex = self.stackPointer[stackNum]
        if lastIndex != self.indexUsed - 1:
            self.swap(lastIndex, self.indexUsed-1, stackNum)

        self.stackPointer[stackNum] = self.buffer[self.stackPointer[stackNum]].prev
        if self.stackPointer[stackNum] != -1:
            self.buffer[self.stackPointer[stackNum]].next = -1

        self.buffer[self.indexUsed-1] = None
        self.indexUsed -= 1
        return value

    def peek(self, stackNum):
        return self.buffer[self.stackPointer[stackNum]].value

    def isEmpty(self, stackNum):
        return self.stackPointer[stackNum] == -1

    def swap(self, lastIndex, topIndex, stackNum):
        if self.buffer[lastIndex].prev == topIndex:
            self.buffer[lastIndex].value, self.buffer[topIndex].value = self.buffer[topIndex].value, self.buffer[lastIndex].value
            tp = self.buffer[topIndex].prev
            if tp != -1:
                self.buffer[tp].next = lastIndex
            self.buffer[lastIndex].prev = tp
            self.buffer[lastIndex].next = topIndex
            self.buffer[topIndex].prev = lastIndex
            self.buffer[topIndex].next = -1
            self.stackPointer[stackNum] = topIndex
            return

        lp = self.buffer[lastIndex].prev
        if lp != -1:
            self.buffer[lp].next = topIndex

        tp = self.buffer[topIndex].prev
        if tp != -1:
            self.buffer[tp].next = lastIndex

        tn = self.buffer[topIndex].next
        if tn != -1:
            self.buffer[tn].prev = lastIndex
        else:
            for i in range(3):
                if self.stackPointer[i] == topIndex:
                    self.stackPointer[i] = lastIndex

        self.buffer[lastIndex], self.buffer[topIndex] = self.buffer[topIndex], self.buffer[lastIndex]
        self.stackPointer[stackNum] = topIndex


class StackNode:
    def __init__(self, p, v, n):
        self.value = v
        self.prev = p
        self.next = n

        
# My own solution. Pretty straightforward, allocates 3 sections in the array, each hosting a stack.
class ThreeStacks:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.array = [None] * (3 * size)
        self.size = size
        self.next_elements_pos = [0, size, 2 * size]
        self.max_pos = [size - 1, 2 * size - 1, 3 * size - 1]

    """
    @param: stackNum: An integer
    @param: value: An integer
    @return: nothing
    """
    def push(self, stackNum, value):
        if self.next_elements_pos[stackNum] > self.max_pos[stackNum]:
            return
        self.array[self.next_elements_pos[stackNum]] = value
        self.next_elements_pos[stackNum] += 1

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def pop(self, stackNum):
        if self.next_elements_pos[stackNum] == stackNum * self.size:
            return None        
        self.next_elements_pos[stackNum] -= 1
        last_element = self.array[self.next_elements_pos[stackNum]]
        self.array[self.next_elements_pos[stackNum]] = None
        return last_element

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def peek(self, stackNum):
        if self.next_elements_pos[stackNum] == stackNum * self.size:
            return None
        return self.array[self.next_elements_pos[stackNum] - 1]

    """
    @param: stackNum: An integer
    @return: true if the stack is empty else false
    """
    def isEmpty(self, stackNum):
        return self.peek(stackNum) is None

        
