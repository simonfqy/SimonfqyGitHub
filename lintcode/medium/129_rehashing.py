"""
https://www.lintcode.com/problem/rehashing/description
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

# My own solution.
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        values = []
        for node in hashTable:
            while node is not None:
                values.append(node.val)
                node = node.next
        size = len(hashTable)
        new_size = size * 2
        new_table = [None] * new_size
        for val in values:
            code = val % new_size
            node = new_table[code]
            if node is None:
                new_table[code] = ListNode(val)
                continue
            
            while node.next is not None:
                node = node.next
            node.next = ListNode(val)
        return new_table
