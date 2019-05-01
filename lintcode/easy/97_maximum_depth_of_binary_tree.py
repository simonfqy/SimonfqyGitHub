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
