'''
Link: https://www.lintcode.com/problem/maximum-depth-of-binary-tree/description
'''

# My own recursive solution.
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    
# Iterative solution using BFS.
from collections import deque
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        depth = 0
        if root is None:
            return depth
        queue = deque([root])
        while queue:
            size = len(queue)
            depth += 1
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return depth
    

# From the Java version of Jiuzhang.com's solution. 遍历 instead of 分治。
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        self.max_depth = 0
        if root is None:
            return self.max_depth
        self.helper(root, 1)
                
        return self.max_depth
        
    def helper(self, root, curr_depth):
        if root is None:
            return
        if curr_depth > self.max_depth:
            self.max_depth = curr_depth
        self.helper(root.left, curr_depth + 1)
        self.helper(root.right, curr_depth + 1)
        
        
# Following a student's solution. Basically just records the depth along with each node 
# as a tuple in the stack.        
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        max_depth = 0
        if root is None:
            return max_depth
        max_depth += 1
        stack = [(root, max_depth)]
        while stack:
            node, depth = stack.pop()
            max_depth = max(depth, max_depth)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
            
        return max_depth
