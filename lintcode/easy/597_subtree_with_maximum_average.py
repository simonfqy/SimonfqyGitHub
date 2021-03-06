"""
Link: https://www.lintcode.com/problem/subtree-with-maximum-average/description
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# My own solution. Uses DFS, divide-and-conquer. Not very succinct.
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        max_root, _, _, _ = self.find_subtree(root)
        return max_root
        
        
    def find_subtree(self, root):
        if root is None:
            return None, None, 0, None
        left_max_subtree_root, left_max_avg, left_subtree_size, left_sum = self.find_subtree(root.left)
        right_max_subtree_root, right_max_avg, right_subtree_size, right_sum = self.find_subtree(root.right)
        total_size = 1
        total_sum = root.val
        son_max_avg = None
        left_bigger = False
        right_bigger = False
        
        if left_sum is not None:
            total_size += left_subtree_size
            total_sum += left_sum
            son_max_avg = left_max_avg
            left_bigger = True
        if right_sum is not None:
            total_size += right_subtree_size
            total_sum += right_sum
            if son_max_avg is None or son_max_avg < right_max_avg:
                son_max_avg = right_max_avg
                left_bigger = False
                right_bigger = True
        
        total_avg = total_sum/total_size
        
        if son_max_avg is None or total_avg > son_max_avg:
            return root, total_avg, total_size, total_sum
        elif left_bigger:
            return left_max_subtree_root, left_max_avg, total_size, total_sum
        else:
            return right_max_subtree_root, right_max_avg, total_size, total_sum
        
        
# My solution based on the solution given in jiuzhang.com. Uses global variables to get rid of some complexities
# involved in comparison and returning. Shortens the code length by a great extent.
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        self.max_average = None
        self.node = None
        self.find_subtree(root)
        return self.node
        
    # Only return size and sum of the subtree starting from the root.
    def find_subtree(self, root):
        if root is None:
            return 0, None
        left_subtree_size, left_sum = self.find_subtree(root.left)
        right_subtree_size, right_sum = self.find_subtree(root.right)
        total_size = 1 + left_subtree_size + right_subtree_size
        total_sum = root.val
        
        if left_sum is not None:
            total_sum += left_sum
        if right_sum is not None:
            total_sum += right_sum
        
        total_avg = total_sum/total_size
        if self.max_average is None or total_avg > self.max_average:
            # The two global variables are modified while traversal, only keeping the best result so far.
            self.max_average = total_avg
            self.node = root
        
        return total_size, total_sum
