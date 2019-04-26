"""
Link: https://www.lintcode.com/problem/binary-tree-preorder-traversal/description
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        stack = [root]
        output_list = []
        while stack:
            node = stack.pop()
            output_list.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return output_list
    
    
# My own solution, 3 months after the previous one.
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        value_list = []
        if root is None:
            return value_list
        stack = [root]
        node = root
        while stack:
            if node is not None:
                value_list.append(node.val)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right
        
        return value_list
