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

# Divide and conquer, but also uses a flag isBST to record the state while traversing the tree.
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        self.lastVal = None
        self.isBST = True
        self.validate(root)
        return self.isBST

    def validate(self, root):
        if root is None:
            return
        self.validate(root.left)
        if self.lastVal is not None and self.lastVal >= root.val:
            self.isBST = False
            return
        self.lastVal = root.val
        self.validate(root.right)
  
# My own solution after 9 months. It is actually similar to the solution provided in jiuzhang's video lecture,
# but more concise.
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        is_bst, _, _ = self.check_validity(root)
        return is_bst
    
    def check_validity(self, root):
        if root is None:
            return True, None, None
            
        left_is_bst, left_min, left_max = self.check_validity(root.left)
        right_is_bst, right_min, right_max = self.check_validity(root.right)
        if not left_is_bst or not right_is_bst:
            return False, None, None
        if left_max is not None and left_max >= root.val:
            return False, None, None
        if right_min is not None and right_min <= root.val:
            return False, None, None
        min_val, max_val = root.val, root.val
        if left_min is not None:
            min_val = left_min
        if right_max is not None:
            max_val = right_max
        return True, min_val, max_val 
