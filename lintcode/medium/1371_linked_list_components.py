'''
Link: https://www.lintcode.com/problem/1371/
'''

# My own solution. Uses union find.
from typing import (
    List,
)
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
    @param head: the head
    @param g: an array
    @return: the number of connected components in G
    """
    def num_components(self, head: ListNode, g: List[int]) -> int:
        num_to_prev = dict()
        num_to_next = dict()
        while head:
            next_node = head.next
            if not next_node:
                break
            num_to_next[head.val] = next_node.val
            num_to_prev[next_node.val] = head.val
            head = next_node
        num_to_parent = dict()
        for this_num in g:
            prev_num_in_linked_list = num_to_prev.get(this_num)
            next_num_in_linked_list = num_to_next.get(this_num)
            num_to_parent[this_num] = this_num
            if prev_num_in_linked_list is not None and prev_num_in_linked_list in num_to_parent:
                num_to_parent[this_num] = num_to_parent[prev_num_in_linked_list]
            if next_num_in_linked_list is not None:
                descendant = next_num_in_linked_list
                # Overwrite the parent of all descendants into the parent of this_num.
                while descendant is not None and descendant in num_to_parent:
                    num_to_parent[descendant] = num_to_parent[this_num]
                    descendant = num_to_next.get(descendant)
        count = len(set([parent for num, parent in num_to_parent.items()]))
        return count


# Solution from jiuzhang.com. Uses set, because we don't need to care about the order of elements inside g.
class Solution:
    """
    @param head: the head
    @param g: an array
    @return: the number of connected components in G
    """
    def num_components(self, head: ListNode, g: List[int]) -> int:
        set_g = set(g)
        count = 0
        while head:
            if head.val in set_g and (not head.next or head.next.val not in set_g):
                count += 1
            head = head.next
        return count
    
    
    
