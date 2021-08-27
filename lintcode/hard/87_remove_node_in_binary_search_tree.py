"""
Link: https://www.lintcode.com/problem/87/
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# My own solution. Using recursion. If the node to be removed has both left and right subtrees, promote the left child to be the
# parent node, and make the right subtree the right child of the rightmost descendant of the original left child (now parent).
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        if not root:
            return root
        if root.val < value:
            root.right = self.removeNode(root.right, value)
            return root
        if root.val > value:
            root.left = self.removeNode(root.left, value)
            return root
        # Now root.val == value
        if not root.left and not root.right:
            return None
        if not root.left and root.right:
            return root.right
        if not root.right and root.left:
            return root.left
        # Root has both left and right subtrees
        left_node = root.left
        while left_node.right:
            left_node = left_node.right
        left_node.right = root.right
        return root.left
