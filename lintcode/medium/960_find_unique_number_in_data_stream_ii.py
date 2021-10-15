'''
Link: https://www.lintcode.com/problem/960/
'''

# My own solution using dictionary and linked list, but largely borrowed from an answer provided by a student on jiuzhang.com
# for question 685:
# https://github.com/simonfqy/SimonfqyGitHub/blob/f5c99afa324732ddc2306c8115d2110facce40f3/lintcode/medium/685_first_unique_number_in_data_stream.py#L95
class Node:
    def __init__(self, val):
        self.val = val
        self.prev, self.next = None, None

class DataStream:

    def __init__(self):
        self.head, self.tail = Node(-1), Node(-1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.val_to_node = dict()
          
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        if num in self.val_to_node and not self.val_to_node[num]:
            return
        if num not in self.val_to_node:
            node = Node(num)
            self.val_to_node[num] = node
            self.add_node(node)
        else:
            node_to_remove = self.val_to_node[num]
            self.val_to_node[num] = None
            self.remove_node(node_to_remove)
        
    def add_node(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def remove_node(self, node):
        prev = node.prev
        next_node = node.next
        prev.next = next_node
        next_node.prev = prev

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        return self.head.next.val
    
    
# Answer from jiuzhang.com. I implemented myself after reading it. It is similar to my solution above, the
# differences are that we only have 1 dummy node which is in the head, rather than 1 in the head and 1 at tail.
# We also have a self.tail pointer to point to the current last node in the linked list. We no longer have self.prev
# pointer in nodes, now we have a self.num_to_prev dictionary to return us the pointer to previous nodes.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class DataStream:

    def __init__(self):
        self.repeated_nums = set()
        self.num_to_prev = dict()
        self.dummy = Node(-1)
        self.tail = self.dummy
          
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        if num in self.repeated_nums:
            return
        if num in self.num_to_prev:
            self.repeated_nums.add(num)
            self.remove(num)
            return
        self.add_node(num)

    def remove(self, num):
        prev = self.num_to_prev[num]
        del self.num_to_prev[num]
        prev.next = prev.next.next
        if prev.next == None:
            self.tail = prev
        else:
            self.num_to_prev[prev.next.val] = prev
    
    def add_node(self, num):
        node = Node(num)
        self.tail.next = node
        self.num_to_prev[num] = self.tail
        self.tail = node                    

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        return self.dummy.next.val
    
    
# My own answer, using OrderedDict.
from collections import OrderedDict
class DataStream:

    def __init__(self):
        self.candidate_unique_nums = OrderedDict()
        self.repeated_nums = set()
          
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        if num in self.repeated_nums:
            return
        if num in self.candidate_unique_nums:
            del self.candidate_unique_nums[num]
            self.repeated_nums.add(num)
            return
        self.candidate_unique_nums[num] = None    

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        for num, _ in self.candidate_unique_nums.items():
            return num
        
        
# This is a O(logN) time complexity solution provided by a student on jiuzhang.com. It uses heap, and
# the self.id field is used for ordering in the heap, because heap uses the first element of the tuple for ordering.
import heapq
class DataStream:

    def __init__(self):
        # do intialization if necessary
        self.heap = []
        self.num_dict = {}
        self.id = 0
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        # write your code here
        self.id += 1
        self.num_dict[num] = self.num_dict.get(num, 0) + 1
        if self.num_dict[num] == 1:
            heapq.heappush(self.heap, (self.id, num))
        
    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        # write your code here
        while self.heap:
            if self.num_dict[self.heap[0][1]] == 1:
                return self.heap[0][1]
            else:
                heapq.heappop(self.heap)
        return -1
