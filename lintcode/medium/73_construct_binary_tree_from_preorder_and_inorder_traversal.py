"""
Link: https://www.lintcode.com/problem/construct-binary-tree-from-preorder-and-inorder-traversal/description
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# My own solution, following the official solution of:
# https://github.com/simonfqy/SimonfqyGitHub/blob/1633979176663e66bd03bc8862980e14a39813e6/lintcode/medium/72_construct_binary_tree_from_inorder_and_postorder_traversal.py#L14
class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if preorder is None or len(preorder) <= 0:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_pos_inorder = inorder.index(root_val)
        left_subtree_size = root_pos_inorder
        root.left = self.buildTree(preorder[1: left_subtree_size + 1], inorder[:left_subtree_size])
        root.right = self.buildTree(preorder[left_subtree_size + 1:], inorder[root_pos_inorder + 1:])
        return root 
