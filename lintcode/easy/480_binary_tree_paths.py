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
        # Leaf node case, so paths_to_return was never populated.
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

    
# This an official answer in jiuzhang.com, I modified it only slightly.
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []
        all_paths = []
        self.dfs(root, [str(root.val)], all_paths)
        return all_paths

    # Modifies the all_paths list passed from the input.
    def dfs(self, root, path, all_paths):
        if not root.left and not root.right:
            all_paths.append('->'.join(path))
            return
        if root.left:
            self.dfs(root.left, path + [str(root.left.val)], all_paths)
        if root.right:
            self.dfs(root.right, path + [str(root.right.val)], all_paths)
            
            
# This also an official answer in jiuzhang.com. It is a traversal, whose only difference from the previous
# solution is that, now we have nodes instead of node values in the "path" parameter of dfs().
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
        all_paths = []
        self.dfs(root, [root], all_paths)
        return all_paths

    def dfs(self, root, path, all_paths):
        if not root:
            return
        if not root.left and not root.right:
            # Remember this syntax in Python for functional programming.
            all_paths.append('->'.join([str(n.val) for n in path]))
        self.dfs(root.left, path + [root.left], all_paths)
        self.dfs(root.right, path + [root.right], all_paths)
            

# This an official answer in jiuzhang.com. It is kind of like post-order traversal.
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
        # 99% 的DFS题，不用单独处理叶子节点
        # 这里需要单独处理的原因是, root为None的结果没有办法用于构造 root 是叶子的结果
        if not root.left and not root.right:
            return [str(root.val)]
        all_paths = []
        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)           
        for path in left_paths + right_paths:
            # The path string is constructed from bottom up, all the way to root.
            all_paths.append(str(root.val) + '->' + path)
        return all_paths
