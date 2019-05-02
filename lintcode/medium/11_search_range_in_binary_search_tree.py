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
