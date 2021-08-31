"""
Link: https://www.lintcode.com/problem/453/
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# My own recursive solution. 
class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        if not root:
            return
        if root.right:
            self.flatten(root.right)
        if root.left:
            self.flatten(root.left)
            node = root.left
            while node.right:
                node = node.right
            node.right = root.right
            root.right = root.left
            root.left = None
