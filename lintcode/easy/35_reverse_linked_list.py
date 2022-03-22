'''
Link: https://www.lintcode.com/problem/35
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

# My own solution. Modifies the list in-place and goes in 1-pass. Has O(n) time and O(1) space complexities.
class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head: ListNode) -> ListNode:
        head_of_reversed_list = None
        cursor = head
        while cursor:
            next_node = cursor.next
            new_head = cursor
            new_head.next = head_of_reversed_list
            head_of_reversed_list = new_head
            cursor = next_node
        return head_of_reversed_list
    
    
# Recursive solution from jiuzhang.com.    
class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        reversed_head = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return reversed_head
    
    
