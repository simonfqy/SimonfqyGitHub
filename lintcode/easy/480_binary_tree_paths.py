"""
https://www.lintcode.com/problem/480/
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# My own solution, uses recursion.
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        return self.get_tree_paths(root, "")

    def get_tree_paths(self, root, path_prefix):
        if not root:
            return []
        if path_prefix == "":
            path_prefix = str(root.val)
        else:
            path_prefix += "->" + str(root.val)
        paths_to_return = []
        if root.left:
            paths_to_return.extend(self.get_tree_paths(root.left, path_prefix))
        if root.right:
            paths_to_return.extend(self.get_tree_paths(root.right, path_prefix))
        if len(paths_to_return) == 0:
            return [path_prefix]
        return paths_to_return
