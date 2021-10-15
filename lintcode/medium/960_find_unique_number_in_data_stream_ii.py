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
