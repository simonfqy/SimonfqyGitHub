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
    
    
# More succinct than the above solution.
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        is_balanced, _ = self.get_balance_status_and_depth(root)
        return is_balanced

    def get_balance_status_and_depth(self, root):
        if not root:
            return True, 0
        left_balanced, left_depth = self.get_balance_status_and_depth(root.left)
        right_balanced, right_depth = self.get_balance_status_and_depth(root.right)
        total_depth = max(right_depth, left_depth) + 1
        return left_balanced and right_balanced and abs(left_depth - right_depth) <= 1, total_depth 
    
    
# My own solution. Uses a helper function to obtain depth.
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        if not root:
            return True
        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)
        if not (left_balanced and right_balanced):
            return False
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        return abs(left_depth - right_depth) <= 1

    def get_depth(self, root):
        if not root:
            return 0
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        return max(left_depth, right_depth) + 1
    
# The only difference from the above solution is the use of dictionary to store the depth of each subtree rooted at a node.
class Solution:
    node_to_depth = dict()
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        if not root:
            return True
        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)
        if not (left_balanced and right_balanced):
            return False
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        return abs(left_depth - right_depth) <= 1

    def get_depth(self, root):
        if not root:
            return 0
        if root in self.node_to_depth:
            return self.node_to_depth[root]
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        depth = max(left_depth, right_depth) + 1
        self.node_to_depth[root] = depth
        return depth
