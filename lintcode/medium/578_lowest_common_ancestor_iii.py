"""
Link: https://www.lintcode.com/problem/578/
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

# My own solution. Uses recursion and a global variable storing LCA.
class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        self.lca = None
        self.get_lca(root, A, B)
        return self.lca

    # return: have_a, have_b
    def get_lca(self, root, A, B):
        if not root:
            return False, False    
        left_has_a, left_has_b = self.get_lca(root.left, A, B)
        right_has_a, right_has_b = self.get_lca(root.right, A, B)
        if self.lca:
            return True, True
        have_a = left_has_a or right_has_a or root == A
        have_b = left_has_b or right_has_b or root == B
        if have_a and have_b:
            self.lca = root
            return True, True
        return have_a, have_b
    
      
# My own solution. Slightly modified from the previous one, uses recursion without global variables.
class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here        
        lca, _, _ = self.get_lca(root, A, B)
        return lca

    # return: lca, have_a, have_b
    def get_lca(self, root, A, B):
        if not root:
            return None, False, False    
        left_lca, left_has_a, left_has_b = self.get_lca(root.left, A, B)
        right_lca, right_has_a, right_has_b = self.get_lca(root.right, A, B)
        if left_lca or right_lca:
            return left_lca or right_lca, True, True
        have_a = left_has_a or right_has_a or root == A
        have_b = left_has_b or right_has_b or root == B
        if have_a and have_b:            
            return root, True, True
        return None, have_a, have_b
