"""
Link: https://www.lintcode.com/problem/balanced-binary-tree/description
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        is_balanced, _ = self.get_depth_and_balanced(root)
        return is_balanced
        
    def get_depth_and_balanced(self, root):
        if root is None:
            return (True, 0)
        left_balanced, left_depth = self.get_depth_and_balanced(root.left)
        if not left_balanced:
            return (False, -1)
        right_balanced, right_depth = self.get_depth_and_balanced(root.right)
        if not right_balanced:
            return (False, -1)
        return (abs(left_depth - right_depth) <= 1, max(left_depth, right_depth) + 1)
