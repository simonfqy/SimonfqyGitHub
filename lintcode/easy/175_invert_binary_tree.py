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
        
