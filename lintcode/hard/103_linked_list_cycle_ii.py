'''
Link: https://www.lintcode.com/problem/linked-list-cycle-ii/description
'''

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

# My own solution which uses set.
class Solution:
    """
    @param head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if head is None:
            return None
        node_set = set()
        node = head
        while node is not None:
            if node in node_set:
                return node
            node_set.add(node)
            node = node.next
        return None
    

# Based on the teaching from Jiuzhang.com. Get the convergence point of the fast and slow pointers,
# where the fast pointer traverses 2 steps at a time and slow pointer 1 at a time. Then, after finding
# the convergence point, designate 1 pointer starting from the head node, another pointer starting from
# the convergence point, and return the node in which they meet. It can be proved mathematically.
class Solution:
    """
    @param head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if head is None:
            return None
        convergence = self.get_convergence(head)
        if convergence is None:
            return None
        node_1, node_2 = head, convergence
        while True:
            if node_1 == node_2:
                return node_1
            node_1 = node_1.next
            node_2 = node_2.next
                
        return None
        
    def get_convergence(self, head):
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None
