"""
Link: https://www.lintcode.com/problem/87/
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# My own solution. Using recursion. If the node to be removed has both left and right subtrees, promote the left child to be the
# parent node, and make the right subtree the right child of the rightmost descendant of the original left child (now parent).
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        if not root:
            return root
        if root.val < value:
            root.right = self.removeNode(root.right, value)
            return root
        if root.val > value:
            root.left = self.removeNode(root.left, value)
            return root
        # Now root.val == value
        if not root.left and not root.right:
            return None
        if not root.left and root.right:
            return root.right
        if not root.right and root.left:
            return root.left
        # Root has both left and right subtrees
        left_node = root.left
        while left_node.right:
            left_node = left_node.right
        left_node.right = root.right
        return root.left
    
    
# My own iterative solution. 
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        if not root:
            return root
        node = root
        prev = None
        # If we don't have the node.val != value condition in the while statement (but defer it as an if condition to break the while loop), when we
        # reach a node whose value is what we want, prev will be equal to this node, instead of being the parent of that node. This isn't what we want. 
        while node and node.val != value:
            prev = node
            if node.val < value:
                node = node.right
            else:
                node = node.left
        # No matching node.
        if not node:
            return root        
        # Matching node found.
        # If prev is None, it means it never entered that while loop. This means the root node
        # is the matching node, hence we simply return the changed root node.
        if not prev:
            return self.obtain_new_value_for_prev_child(node)
        if prev.val < value:
            # If we directly assign this value to node, it will not work. We have to modify the link from prev node to the modified node,
            # hence we need to use prev node.
            prev.right = self.obtain_new_value_for_prev_child(node)
        else:
            prev.left = self.obtain_new_value_for_prev_child(node)
        return root

    def obtain_new_value_for_prev_child(self, node):
        if not (node.left or node.right):
            return None
        if node.left and not node.right:
            return node.left
        if node.right and not node.left:
            return node.right
        left_node = node.left
        while left_node.right:            
            left_node = left_node.right
        left_node.right = node.right
        return node.left
