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

    
# Another of my solution. Uses recursive method.
import math
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        if root is None:
            return True
        if not self.is_valid(root.left, -math.inf, root.val):
            return False
        return self.is_valid(root.right, root.val, math.inf)
        
    def is_valid(self, root, lower_bound, upper_bound):
        if root is None:
            return True
        root_val = root.val
        if root_val <= lower_bound or root_val >= upper_bound:
            return False
        return (self.is_valid(root.left, lower_bound, root_val) and self.is_valid(
            root.right, root_val, upper_bound))
 

# Copied from the Java version in Jiuzhang's video lectures.   
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        if root is None:
            return True
        is_bst, _, _ = self.get_validity_and_extremes(root)
        return is_bst
        
    def get_validity_and_extremes(self, root):
        if root is None:
            return True, None, None
        root_val = root.val
        left_is_bst, left_min, left_max = self.get_validity_and_extremes(root.left)
        if not left_is_bst or (left_max is not None and left_max >= root_val):
            return False, None, None
        right_is_bst, right_min, right_max = self.get_validity_and_extremes(root.right)
        if not right_is_bst or (right_min is not None and right_min <= root_val):
            return False, None, None
        if left_min is not None:
            min_val = left_min
        else:
            min_val = root_val
        if right_max is not None:
            max_val = right_max
        else:
            max_val = root_val
        return True, min_val, max_val
