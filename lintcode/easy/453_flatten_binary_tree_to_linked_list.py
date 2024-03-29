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
            
            
# A recursive solution provided by a student of jiuzhang.com which makes use of global variable.
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
        # It is kind of a trick to use this order. First go to the right subtree, then to left.
        # If you track how the value of self.last_node changes throughout the recursion, you'll
        # realize that it will set the right child of the last descendant (using preorder traversal) 
        # of the root's left subtree to be the right child of the root. It is not very easy to see
        # from a glance.
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.last_node
        root.left = None
        self.last_node = root

            
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
                
                
# An iterative solution provided by jiuzhang.com. I translated it from Java to Python. It is similar to my iterative solution
# above, but is simpler because it doesn't make use of a prev node. Instead, it uses current node directly.
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
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if stack:
                node.right = stack[-1]
                node.left = None
                
                
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
        
        
# Another recursive solution provided by jiuzhang.com. It uses a helper function to flatten the tree and return the last node. 
class Solution:    
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        self.flatten_and_get_last_node(root)

    def flatten_and_get_last_node(self, root):
        if not root:
            return None
        left_last = self.flatten_and_get_last_node(root.left)
        right_last = self.flatten_and_get_last_node(root.right)
        if left_last:
            left_last.right = root.right
            root.right = root.left
            root.left = None       
        # This is a compact statement which returns the first non-null entity. 
        return right_last or left_last or root   
  
