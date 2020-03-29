"""
Link: https://www.lintcode.com/problem/lowest-common-ancestor-of-a-binary-tree/description
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# This is my own solution using recursion. Not very concise.
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the lowest common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        self.path = []
        self.get_path(root, A)
        path_A = list(self.path)
        self.path = []
        self.get_path(root, B)
        lca_candidate = root
        for i in range(min(len(path_A), len(self.path))):
            if path_A[i] == self.path[i]:
                lca_candidate = path_A[i]
            else:
                break
        return lca_candidate
            
    def get_path(self, root, target):
        if root is None:
            return False
        while len(self.path) > 0:
            last_node = self.path[-1]
            if last_node.left != root and last_node.right != root:
                self.path.pop()
            else:
                break
        self.path.append(root)
        if root.val == target.val:
            return True
        if (self.get_path(root.left, target)):
            return True
        return self.get_path(root.right, target)
