"""
Link: https://www.lintcode.com/problem/binary-tree-postorder-traversal/description
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        val_list = []
        if root is None:
            return val_list
        # Use two stacks to deal with it.
        stack_1 = [root]
        stack_2 = []
        while stack_1:
            node = stack_1.pop()
            stack_2.append(node)
            if node.left:
                stack_1.append(node.left)
            if node.right:
                stack_1.append(node.right)
        
        while stack_2:
            node = stack_2.pop()
            val_list.append(node.val)
        
        return val_list
