"""
URL: https://www.lintcode.com/problem/invert-binary-tree/description
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# My own solution, simple recursion.
class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        # write your code here
        if root is None:
            return
        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)
        root.left, root.right = root.right, root.left
        
# I referred to a solution provided by a student on Jiuzhang.com. It uses BFS, very simple. Next time I should
# think about using BFS first when facing problems related to trees. I was always thinking about DFS and cannot
# figure out a way to do it non-recursively.
from collections import deque
class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        # write your code here
        if root is None:
            return
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
