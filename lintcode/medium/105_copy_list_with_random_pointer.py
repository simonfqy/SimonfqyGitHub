'''
https://www.lintcode.com/problem/105/
'''

# My own solution. Completes the copy process with 1 traversal, using a dictionary (hashmap) to map the
# original nodes to the copied nodes.
"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        copy_head = RandomListNode(head.label)
        node = copy_head
        orig_node = head
        orig_to_new_node = {head: copy_head}
        while orig_node:
            if orig_node.next:                
                if orig_node.next not in orig_to_new_node:
                    # Create a new node based on it
                    next_node = RandomListNode(orig_node.next.label)
                    node.next = next_node
                    orig_to_new_node[orig_node.next] = next_node
                else:
                    # Already created
                    next_node = orig_to_new_node[orig_node.next]
                    node.next = next_node
            if orig_node.random:
                if orig_node.random not in orig_to_new_node:
                    random_node = RandomListNode(orig_node.random.label)
                    node.random = random_node
                    orig_to_new_node[orig_node.random] = random_node
                else:
                    random_node = orig_to_new_node[orig_node.random]
                    node.random = random_node                
            node = node.next
            orig_node = orig_node.next
        return copy_head
