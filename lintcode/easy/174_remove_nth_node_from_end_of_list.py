'''
Link: https://www.lintcode.com/problem/174
'''

# My own solution. Uses 2 pointers.
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        fast, slow = head, head
        gap = 0
        list_size = 1
        while fast:
            if not fast.next:
                if list_size > n:
                    slow.next = slow.next.next
                else:
                    # Handle the special situation where number of nodes in the list is n.
                    return head.next
                break                
            fast = fast.next
            list_size += 1
            if gap < n:
                gap += 1
                continue
            slow = slow.next
        return head
