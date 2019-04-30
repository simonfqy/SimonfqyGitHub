'''
Link: https://www.lintcode.com/problem/construct-binary-tree-from-inorder-and-postorder-traversal/description
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# My own solution after trial and error for a long time.
class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        if len(inorder) <= 0 or inorder is None:
            return None
        last_ind = len(inorder) - 1
        return self.get_subtree(inorder, postorder, 0, last_ind, 0, last_ind)

        
    def get_subtree(self, inorder, postorder, in_start_ind, in_end_ind, post_start_ind,
        post_end_ind):
        if in_start_ind > in_end_ind or post_start_ind > post_end_ind:
            return None
        if in_start_ind == in_end_ind and post_start_ind == post_end_ind:
            return TreeNode(inorder[in_start_ind])
            
        root_val = postorder[post_end_ind]
        root = TreeNode(root_val)
        inorder_root_pos = inorder.index(root_val)
        left_subtree_size = inorder_root_pos - in_start_ind
        root.left = self.get_subtree(inorder, postorder, in_start_ind, 
            in_start_ind + left_subtree_size - 1, post_start_ind, 
            post_start_ind + left_subtree_size - 1)
        right_subtree_size = in_end_ind - inorder_root_pos
        root.right = self.get_subtree(inorder, postorder, in_end_ind - right_subtree_size + 1, 
            in_end_ind, post_end_ind - right_subtree_size, post_end_ind - 1)
        return root
