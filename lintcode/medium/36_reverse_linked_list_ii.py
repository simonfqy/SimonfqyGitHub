'''
Link: https://www.lintcode.com/problem/36/
'''

from lintcode import (
    ListNode,
)

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

# My own solution. Modifies the linked list in-place and in 1-pass. O(n) time complexity.
class Solution:
    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverse_between(self, head: ListNode, m: int, n: int) -> ListNode:
        cursor = head
        order = 1
        node_immediately_before_reversed_section = None
        reversed_section_head = None
        reversed_section_tail = None
        while cursor:
            next_node = cursor.next
            if order == m - 1:
                node_immediately_before_reversed_section = cursor
            if order >= m and order <= n:
                if order == m:
                    reversed_section_tail = cursor
                new_reversed_head = cursor
                new_reversed_head.next = reversed_section_head
                reversed_section_head = new_reversed_head
            if order > n:
                reversed_section_tail.next = cursor
                break
            cursor = next_node
            order += 1
        if node_immediately_before_reversed_section:
            node_immediately_before_reversed_section.next = reversed_section_head
            return head        
        return reversed_section_head
      
      
