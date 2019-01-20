"""
https://www.lintcode.com/problem/binary-tree-level-order-traversal/description
My solution is using level order BFS traversal.
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        queue = deque()
        ret_list = []
        if root is None:
            return ret_list
        queue.append(root)
        while queue:
            size = len(queue)
            this_level_elements = []
            for _ in range(size):
                head = queue.popleft()
                if head is None:
                    continue
                this_level_elements.append(head.val)
                if head.left is not None:
                    queue.append(head.left)
                if head.right is not None:
                    queue.append(head.right)
            ret_list.append(this_level_elements)
        return ret_list
