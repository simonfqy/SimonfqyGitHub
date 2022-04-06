'''
Link: https://www.lintcode.com/problem/1609/
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

# My own solution. Uses two pointers.
class Solution:
    """
    @param head: the head node
    @return: the middle node
    """
    def middle_node(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while fast:
            fast = fast.next
            if not fast:
                break
            slow = slow.next
            fast = fast.next
        return slow
      
      
