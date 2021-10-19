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
