'''
Link: https://www.lintcode.com/problem/1181/
'''

# My solution based on https://labuladong.github.io/algo/di-ling-zh-bfe1b/dong-ge-da-334dd/.
class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        self.max_diameter = 0
        self.max_depth(root)
        return self.max_diameter

    def max_depth(self, root):
        if not root:
            return 0
        left_max_depth = self.max_depth(root.left)
        right_max_depth = self.max_depth(root.right)
        current_level_diameter = left_max_depth + right_max_depth
        self.max_diameter = max(self.max_diameter, current_level_diameter)
        return 1 + max(left_max_depth, right_max_depth)
      
      
