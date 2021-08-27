"""
Link: https://www.lintcode.com/problem/85/
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# Straightforward recursive solution.
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here        
        if not root:
            return node
        if root.val < node.val:
            root.right = self.insertNode(root.right, node)
        if root.val > node.val:
            root.left = self.insertNode(root.left, node)
        return root
    
    
# A variation of the solution in jiuzhang.com which is right below this one.
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here        
        if not root:
            return node
        currt = root
        while True:
            if currt.val > node.val:                
                if not currt.left:
                    currt.left = node
                    break
                currt = currt.left
            else:
                if not currt.right:
                    currt.right = node
                    break
                currt = currt.right
        return root
    
    
# The solution in jiuzhang.com, which doesn't use recursion. 
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here        
        if not root:
            return node
        currt = root
        while currt != node:
            if currt.val > node.val:                
                if not currt.left:
                    currt.left = node                    
                currt = currt.left
            else:
                if not currt.right:
                    currt.right = node                    
                currt = currt.right
        return root
    
    
# A variant of a solution from a student on jiuzhang.com. I did not use a prev node as the original author did. 
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here        
        if not root:
            return node
        cur = root
        while True:
            candidate = cur.left if cur.val > node.val else cur.right
            if candidate:
                cur = candidate
            else:
                break
        if cur.val > node.val:
            cur.left = node
        else:
            cur.right = node
        return root
    
    
# The solution from a student on jiuzhang.com. You can see a prev node being used. The original code was in Java,
# I translated it into Python.
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here        
        if not root:
            return node
        cur = root
        prev = None
        while cur:
            prev = cur
            cur = cur.left if cur.val > node.val else cur.right
        if prev.val > node.val:
            prev.left = node
        else:
            prev.right = node
        return root
