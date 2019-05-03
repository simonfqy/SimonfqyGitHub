'''
Link: https://www.lintcode.com/problem/closest-binary-search-tree-value/description
'''

# My own solution. Uses the property of BST. O(logn) time complexity.
import math
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        curr_closest = math.inf
        return self.recurse_tree(root, target, curr_closest)
        
    def recurse_tree(self, root, target, curr_closest):
        if root is None:
            return curr_closest
        if abs(root.val - target) < abs(curr_closest - target):
            curr_closest = root.val
            if root.val == target:
                return curr_closest
        if root.val < target:
            right_closest = self.recurse_tree(root.right, target, curr_closest)
            if abs(right_closest - target) < abs(curr_closest - target):
                return right_closest
        elif root.val > target:
            left_closest = self.recurse_tree(root.left, target, curr_closest)
            if abs(left_closest - target) < abs(curr_closest - target):
                return left_closest
        return curr_closest
