"""
Link: https://www.lintcode.com/problem/minimum-subtree/description
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# My own solution.
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        self.root_to_subtree_sum = dict()
        self.get_subtree_sum(root)
        min_subtree_root, _ = self.get_min_subtree_sum_and_root(root)
        return min_subtree_root
        
    def get_subtree_sum(self, root):
        left_sum, right_sum = 0, 0
        if root.left:
            left_sum = self.get_subtree_sum(root.left)
        if root.right:
            right_sum = self.get_subtree_sum(root.right)
        total_sum = left_sum + right_sum + root.val
        self.root_to_subtree_sum[root] = total_sum
        return total_sum
    
    def get_min_subtree_sum_and_root(self, root):
        min_subtree_root = root
        min_sum = self.root_to_subtree_sum[root]
        if root.left:
            left_min_subtree_root, left_min_sum = self.get_min_subtree_sum_and_root(root.left)
            if left_min_sum < min_sum:
                min_sum = left_min_sum
                min_subtree_root = left_min_subtree_root
        if root.right:
            right_min_subtree_root, right_min_sum = self.get_min_subtree_sum_and_root(root.right)
            if right_min_sum < min_sum:
                min_sum = right_min_sum
                min_subtree_root = right_min_subtree_root
        return min_subtree_root, min_sum
    
    
