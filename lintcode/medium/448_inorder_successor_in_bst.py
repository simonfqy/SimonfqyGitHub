"""
Link: https://www.lintcode.com/problem/448/
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
# My own solution, using the in-order traversal.
class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        stack = []
        node = root
        get_next = False
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if get_next:
                    return node
                if node == p:
                    get_next = True
                node = node.right
        return None
    
# Another of my solution. Has O(h) time complexity, where h is the height of the BST.    
class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not p:
            return None
        path_to_p = self.get_path_to_p(root, p, [])
        # If p has a right subtree, find the leftmost element of this subtree. That is the successor.
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node
        # p doesn't have a right subtree. So we need to go up from p and find the first node whose left subtree contains p, which is the successor.
        n = path_to_p.pop()
        while path_to_p and path_to_p[-1].right == n:
            n = path_to_p.pop()
        if path_to_p:
            return path_to_p[-1]
        return None
    
    # return: a list of nodes forming the path to p
    def get_path_to_p(self, root, p, path):
        if root is None:
            return path
        path_to_be_returned = list(path)
        path_to_be_returned.append(root)
        if root == p:
            return path_to_be_returned
        if root.val > p.val:
            return self.get_path_to_p(root.left, p, path_to_be_returned)
        return self.get_path_to_p(root.right, p, path_to_be_returned)
    
    
# This solution comes from Jiuzhang.com.
class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        # First, find the position of p and set a candidate successor.
        successor = None
        while root and p.val != root.val:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        # p is not found. Hence no successor.
        if not root:
            return None 
        # p does not have a right subtree. Hence the successor previously assigned is the true successor.
        if not root.right:
            return successor
        # p has a right subtree. Then pick the leftmost node from its right subtree.
        root = root.right
        while root:
            if not root.left:
                return root 
            root = root.left
