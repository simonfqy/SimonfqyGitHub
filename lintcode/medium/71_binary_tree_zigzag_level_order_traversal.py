'''
Link: https://www.lintcode.com/problem/71/
This question was (informally) asked in the Lululemon interview in Mar 2023. During the 8 min during 
the interview, I couldn't think of a concrete solution.
'''

from typing import (
    List,
)
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# My own solution. Uses stack to keep track of the nodes, it's correct but more complicated than the 
# optimal solution.
class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzag_level_order(self, root: TreeNode) -> List[List[int]]:
        results = []
        if not root:
            return results
        curr_stack, next_stack = [root], []
        left_child_first = True
        while curr_stack or next_stack:
            curr_level_vals = []
            while curr_stack:
                node = curr_stack.pop()
                curr_level_vals.append(node.val)
                if left_child_first:
                    if node.left:
                        next_stack.append(node.left)
                    if node.right:
                        next_stack.append(node.right)
                else:
                    if node.right:
                        next_stack.append(node.right)
                    if node.left:
                        next_stack.append(node.left)
            # Go to the next level
            results.append(curr_level_vals)
            curr_stack, next_stack = next_stack, curr_stack
            left_child_first = not left_child_first

        return results


# My implementation of a solution from jiuzhang.com. It is simpler than my own solution above.
from collections import deque
class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzag_level_order(self, root: TreeNode) -> List[List[int]]:
        results = []
        if not root:
            return results
        queue = deque([root])
        left_to_right = 1
        while queue:
            this_level_vals = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                this_level_vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            this_level_vals = this_level_vals[::left_to_right]
            results.append(this_level_vals)
            left_to_right *= -1

        return results
    
