"""
Link: https://www.lintcode.com/problem/binary-tree-postorder-traversal/description
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        val_list = []
        if root is None:
            return val_list
        # Use two stacks to deal with it.
        stack_1 = [root]
        stack_2 = []
        while stack_1:
            node = stack_1.pop()
            stack_2.append(node)
            if node.left:
                stack_1.append(node.left)
            if node.right:
                stack_1.append(node.right)
        
        while stack_2:
            node = stack_2.pop()
            val_list.append(node.val)
        
        return val_list
    
    
# An iterative implementation which only relies on 1 list (stack). It is very similar to the
# iterative in-order traversal. This solution comes from a student in jiuzhang.com:
# https://github.com/simonfqy/SimonfqyGitHub/blob/b23e54bd9f144a7dcb4a2af342f48a501361cf52/lintcode/easy/93_balanced_binary_tree.py#L112
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        stack = []
        return_array = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left or root.right
            else:
                root = stack.pop()
                return_array.append(root.val)
                if stack and root == stack[-1].left:
                    root = stack[-1].right
                else:
                    root = None
        return return_array
