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

    
# 本参考程序来自九章算法，由 @吴助教 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

# Uses iteration instead of recursion. Pretty succinct.
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        upper = root
        lower = root
        while root:
            if target > root.val:
                lower = root
                root = root.right
            elif target < root.val:
                upper = root
                root = root.left
            else:
                return root.val
        if abs(upper.val - target) <= abs(lower.val - target):
            return upper.val
        return lower.val
    
    
# My own solution. Uses iterative approach.
import sys
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        self.closest = None
        self.min_diff = sys.maxsize
        while root:
            if abs(root.val - target) < self.min_diff:
                self.closest = root
                self.min_diff = abs(root.val - target)
            if root.val < target:
                root = root.right
            elif root.val > target:
                root = root.left
            else:
                break
        return self.closest.val
