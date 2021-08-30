"""
https://www.lintcode.com/problem/480/
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# My own solution, uses recursion.
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []            
        return self.get_tree_paths(root, "")

    def get_tree_paths(self, root, path_prefix):        
        if path_prefix == "":
            path_prefix = str(root.val)
        else:
            path_prefix += "->" + str(root.val)
        paths_to_return = []
        if root.left:
            paths_to_return.extend(self.get_tree_paths(root.left, path_prefix))
        if root.right:
            paths_to_return.extend(self.get_tree_paths(root.right, path_prefix))
        if len(paths_to_return) == 0:
            return [path_prefix]
        return paths_to_return
    
    
# This is using BFS, in which each entry stores a node and its corresponding path prefix. This is based
# on a student's answer in jiuzhang.com.
from collections import deque
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
        # Every string in the tuple is the path leading to the current node.
        queue = deque([(root, '')])        
        all_paths = []
        while queue:
            node, path_str = queue.pop()
            # Add the current node to the end of the path to make it complete.
            if path_str != '':
                path_str += "->"
            path_str += str(node.val)
            if node.left or node.right:
                # Not a leaf node.                
                if node.left:
                    queue.appendleft((node.left, path_str))  
                if node.right:
                    queue.appendleft((node.right, path_str))              
            else:
                all_paths.append(path_str)
        return all_paths
