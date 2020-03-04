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
    
    
# I wrote this solution after reading the solution provided on jiuzhang.com.
import sys
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        _, subtree_root, _ = self.get_minimum_subtree_and_sum(root)
        return subtree_root
    
    # Returns: subtree sum, minimum sum subtree root, minimum subtree sum value.
    # I did not think about returning 3 results as a tuple, I only thought about returning 2 simultaneously.
    # Returning all 3 really helps, since they are all necessary to construct the results.
    def get_minimum_subtree_and_sum(self, root):
        # The important part is being able to handle the None case. It can save us from having lots
        # of "if"s to check whether the left or right subtree exists, simplifying the code quite a bit. Otherwise
        # it becomes very long, complicated and dirty.
        if root is None:
            return 0, None, sys.maxsize # using sys.maxsize is very important here, ensures correctness.
        # Since None root case is considered, we can directly run the function recursively on both subtrees without
        # checking for the existence of the subtree. Saves lots of hassle.
        left_sum, left_min_subtree, left_min_sum = self.get_minimum_subtree_and_sum(root.left)
        right_sum, right_min_subtree, right_min_sum = self.get_minimum_subtree_and_sum(root.right)
        root_sum = left_sum + right_sum + root.val
        # Only 3 possibilities exist for the min sum subtree: either the min sum subtree of left subtree, that of the
        # right subtree, or the whole tree. In this case the root_sum is the minimum subtree sum.
        if root_sum == min(left_min_sum, right_min_sum, root_sum):
            return root_sum, root, root_sum
        if left_min_sum < right_min_sum:
            return root_sum, left_min_subtree, left_min_sum
        # The only case left is the min right subtree is the min sum subtree of this whole tree.
        return root_sum, right_min_subtree, right_min_sum
    
    # Overall thinking: it is quite hard to know what is the right thing to do. When you are handling None case for the
    # recursive function, if you do other parts wrongly, the function will also be quite complicated (for example, I did not
    # think about returning a tuple of 3, only returning a 2-tuple, making the recursive function very hard to implement).
    # As a general rule of thumb, let your recursive function handle the None case, and try to fix the other problems should 
    # there arise any, rather than disabling the None handling logic in the recursive function. 
    
    # 3 elements are most important for 1 recursive function to be enough: subtree sum, minimum sum subtree root, minimum 
    # subtree sum value. All of them are indispensable.
    # I have to realize this when designing or implementing this recursive function.
    
