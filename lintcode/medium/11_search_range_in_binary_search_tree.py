'''
Link: https://www.lintcode.com/problem/search-range-in-binary-search-tree/description
'''

# My own solution, uses iterative inorder traversal.
class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        key_list = []
        if k1 > k2 or root is None:
            return key_list
            
        stack = []
        node = root
        while stack or node:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if k1 <= node.val and k2 >= node.val:
                    key_list.append(node.val)
                node = node.right
        return key_list

    
# Also my own solution, using recursive inorder traversal.
class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        key_list = []
        if k1 > k2 or root is None:
            return key_list
        key_list = self.get_suitable_key_list(root, k1, k2)    
        
        return key_list      
    
    def get_suitable_key_list(self, root, k1, k2):
        key_list = []
        if root is None:
            return key_list
        
        if root.val >= k1:
            key_list.extend(self.get_suitable_key_list(root.left, k1, k2))
        if root.val >= k1 and root.val <= k2:
            key_list.append(root.val)
        if root.val <= k2:
            key_list.extend(self.get_suitable_key_list(root.right, k1, k2))
        return key_list
    
    
# Recursive solution. Conceptually similar to the one above, but more concise.
class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        if not root:
            return []
        left_range = self.searchRange(root.left, k1, k2)
        right_range = self.searchRange(root.right, k1, k2)
        if root.val >= k1 and root.val <= k2:
            return left_range + [root.val] + right_range
        if root.val < k1:
            return right_range
        if root.val > k2:
            return left_range
    
    
# This is the solution from Jiuzhang.com. Iterative.
class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        return_list = []
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                node = stack[-1]
                if node.val >= k1 and node.val <= k2:
                    return_list.append(node.val)
        return return_list
