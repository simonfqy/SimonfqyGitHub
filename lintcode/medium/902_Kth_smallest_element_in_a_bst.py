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
    

# My own recursive solution based on the solution provided in jiuzhang.com. Uses a global dict to store the subtree sizes.
class Solution:
    node_to_subtree_size = dict()
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        if not root:
            return None
        left_node_count = self.get_node_count(root.left)
        if left_node_count >= k:
            return self.kthSmallest(root.left, k)
        if left_node_count == k - 1:
            return root.val
        return self.kthSmallest(root.right, k - left_node_count - 1)

    def get_node_count(self, root):
        if not root:
            return 0
        if root in self.node_to_subtree_size:
            return self.node_to_subtree_size[root]
        left_count = self.get_node_count(root.left)
        right_count = self.get_node_count(root.right)
        total_count = left_count + right_count + 1
        self.node_to_subtree_size[root] = total_count
        return total_count
    
    
# A solution from jiuzhang.com. Similar to the binary tree iterator: 
# https://github.com/simonfqy/SimonfqyGitHub/blob/0123e427d382c53293720f3c1c907ba71e66640f/lintcode/easy/67_binary_tree_inorder_traversal.py#L81
class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # use binary tree iterator
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        for _ in range(k):
            node = stack.pop()
            if node.right:
                right_node = node.right
                while right_node:
                    stack.append(right_node)
                    right_node = right_node.left
            if not stack:
                return None
        return stack[-1].val
