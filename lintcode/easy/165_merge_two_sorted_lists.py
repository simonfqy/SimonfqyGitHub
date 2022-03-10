'''
Link: https://www.lintcode.com/problem/165/
'''

# My own solution. This question got asked in the Wish virtual onsite interview and caught me somewhat off guard. I implemented
# a linked list class by myself, which is actually unnecessary. 
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

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged_head = ListNode(None)
        cursor = merged_head
        while l1 and l2:
            if l1.val <= l2.val:
                cursor.next = l1
                l1 = l1.next
            else:
                cursor.next = l2
                l2 = l2.next
            cursor = cursor.next
        if l1:
            cursor.next = l1
        else:
            cursor.next = l2
        return merged_head.next

      
