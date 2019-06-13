"""
https://www.lintcode.com/problem/kth-smallest-element-in-a-bst/description
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# My own solution, using inorder traversal template in jiuzhang.com.
class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        if root is None or k <= 0:
            return None
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        counter = 0
        
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                counter += 1
                if counter == k:
                    return stack[-1].val
        return None
