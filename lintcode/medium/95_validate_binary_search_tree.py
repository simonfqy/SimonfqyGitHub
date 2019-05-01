"""
https://www.lintcode.com/problem/validate-binary-search-tree/description
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# My own solution: a straightforward implementation of in-order traversal to determine the validity.
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        if root is None:
            return True
        stack = []
        node = root
        prev = None
        while stack or node:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if prev is not None and prev.val >= node.val:
                    return False
                prev = node
                node = node.right
        return True
