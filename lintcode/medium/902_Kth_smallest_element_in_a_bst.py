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

    
# Using the inorder traversal from stackoverflow.
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
        node = root
        stack = []
        counter = 0
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                counter += 1
                if counter == k:
                    return node.val
                node = node.right
                
        return None
    
# Using the Java example from Jiuzhang.com. Divide-and-conquer, similar to quickSelect algorithm. Performs well for 
# repeated reads.
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
        subtree_element_count = dict()
        self.get_element_counts(root, subtree_element_count)
        return self.get_kth_smallest(root, k, subtree_element_count)
        
    def get_element_counts(self, root, subtree_element_count):
        if root is None:
            return 0
        left_count = self.get_element_counts(root.left, subtree_element_count)
        right_count = self.get_element_counts(root.right, subtree_element_count)
        total_count = left_count + right_count + 1
        subtree_element_count[root] = total_count
        return total_count
        
    def get_kth_smallest(self, root, k, subtree_element_count):
        if k <= 0 or k > subtree_element_count[root]:
            return None
        if root.left:
            left_count = subtree_element_count[root.left]
        else:
            left_count = 0
        if left_count >= k:
            return self.get_kth_smallest(root.left, k, subtree_element_count)
        if k == left_count + 1:
            return root.val
        # k > left_count + 1
        return self.get_kth_smallest(root.right, k - left_count - 1, subtree_element_count)


