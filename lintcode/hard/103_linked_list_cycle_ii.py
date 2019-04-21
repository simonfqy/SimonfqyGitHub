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
