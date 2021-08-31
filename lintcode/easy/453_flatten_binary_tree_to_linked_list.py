"""
Link: https://www.lintcode.com/problem/453/
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# My own recursive solution. 
class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        if not root:
            return
        if root.right:
            self.flatten(root.right)
        if root.left:
            self.flatten(root.left)
            node = root.left
            while node.right:
                node = node.right
            node.right = root.right
            root.right = root.left
            root.left = None # This assignment is crucial, don't forget it.

            
# My own iterative solution. 
class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        if not root:
            return
        stack = [root]
        prev = None
        while stack:
            node = stack.pop()
            if prev:
                prev.right = node
                prev.left = None # This assignment is crucial, don't forget it.
            prev = node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
                
# Recursive solution provided by jiuzhang.com. Uses a global variable last_node. 
class Solution:
    last_node = None
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        if not root:
            return
        if self.last_node:
            self.last_node.left = None
            self.last_node.right = root
        self.last_node = root
        # This assignment is required. Otherwise, when self.flatten(root.left) is called, the root.right is modified 
        # because root is the last_node in that function. So we need to keep a copy here.
        right = root.right
        self.flatten(root.left)        
        self.flatten(right) 
