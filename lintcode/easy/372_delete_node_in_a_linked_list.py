'''
Link: https://www.lintcode.com/problem/372
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

# My own solution.
class Solution:
    """
    @param: node: the node in the list should be deleted
    @return: nothing
    """
    def deleteNode(self, node):
        if not node:
            return
        next_node = node.next
        curr_node = node
        while next_node:
            curr_node.val = next_node.val
            curr_node.next = next_node.next
            # Previously I wrote it to be curr_node = next_node, it resulted in errors.
            curr_node = curr_node.next
            next_node = next_node.next
            
            
# My solution, optimized from the one above. It's actually very simple. We just need to replicate the current node to the next node, 
# then change the pointer to the second next node of the current node, then we're done.  
class Solution:
    """
    @param: node: the node in the list should be deleted
    @return: nothing
    """
    def deleteNode(self, node):
        if not node:
            return
        next_node = node.next
        curr_node = node
        if next_node:
            curr_node.val = next_node.val
            curr_node.next = next_node.next
            
            
# A more succinct solution from lintcode.com.  
class Solution:
    """
    @param: node: the node in the list should be deleted
    @return: nothing
    """
    def deleteNode(self, node):
        # write your code here
        if not node or not node.next:
            node = None
            return

        node.val = node.next.val
        node.next = node.next.next
