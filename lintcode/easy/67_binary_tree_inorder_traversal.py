'''
https://www.lintcode.com/problem/binary-tree-inorder-traversal/description
Can refer to this: 
https://github.com/simonfqy/SimonfqyGitHub/blob/c6111760e973df45c8291bc739198db9120063f5/algorithms/DFS_and_different_traversals.py#L61
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# The iterative version. Done by myself.
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        output_list = []
        if root is None:
            return output_list
        stack = []
        node = root
        while stack or node:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                output_list.append(node.val)
                node = node.right
            
        return output_list
