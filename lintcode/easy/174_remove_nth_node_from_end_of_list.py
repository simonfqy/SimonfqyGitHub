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
    
    
# My own solution. Slightly optimized from the one above, does not require getting the length of the linked list.
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        fast, slow = head, head
        gap = 0
        while fast:
            if not fast.next:
                if gap >= n:
                    slow.next = slow.next.next
                else:
                    # Handle the special situation where number of nodes in the list is n.
                    return head.next
                break                
            fast = fast.next
            if gap < n:
                gap += 1
                continue
            slow = slow.next
        return head
    
    
# My own solution. Slightly modified from the one above by adding a dummy node in the beginning so we don' t need
# to treat the case where list size == n separately. It simplifies the logic.
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1, head)
        fast, slow = dummy, dummy
        gap = 0
        while fast:
            if not fast.next:                
                slow.next = slow.next.next
                break                
            fast = fast.next
            if gap < n:
                gap += 1
                continue
            slow = slow.next
        return dummy.next
    
    
# Solution from lintcode.com. It is similar to my own solution above, but it is slightly clearer.
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1, head)
        # Note that slow starts from dummy but fast starts from head.
        slow, fast = dummy, head
        for _ in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

    
# This solution is very similar from the one above. Just the fast pointer is initialized to dummy rather than head.    
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:        
        dummy = ListNode(None, head)
        fast, slow = dummy, dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
    
    
