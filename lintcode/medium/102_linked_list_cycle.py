'''
Link: https://www.lintcode.com/problem/linked-list-cycle/description
'''
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

# Based on the teachings from Jiuzhang.com. Uses two pointers.
class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if head is None:
            return False
        slow = head
        fast = head.next
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    
# Another of my solution using set.    
class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here        
        current = head
        node_set = set()
        while current is not None:
            if current in node_set:
                return True
            node_set.add(current)
            current = current.next
        return False

   
# Another two pointer solution. Simpler than the one above.
class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
    
    
