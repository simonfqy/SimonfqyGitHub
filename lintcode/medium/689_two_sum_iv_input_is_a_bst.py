'''
Link: https://www.lintcode.com/problem/two-sum-iv-input-is-a-bst/description
'''

# This solution is my own. Based on the two sum, using two pointers, but here we traverse the BST.
# We have to use global variable to track the position of the current node in tree traversal.
class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        # write your code here
        self.left_stack = []
        self.right_stack = []
        self.left_node, self.left_node_to_push = None, root
        self.right_node, self.right_node_to_push = None, root
        self.get_left_node()
        self.get_right_node()
        while self.left_node != self.right_node:
            if self.left_node.val + self.right_node.val == n:
                return [self.left_node.val, self.right_node.val]
            if self.left_node.val + self.right_node.val < n:
                self.get_left_node()
            else:
                self.get_right_node()
        return
    
    
    def get_left_node(self):
        while self.left_stack or self.left_node_to_push:
            if self.left_node_to_push is not None:
                self.left_stack.append(self.left_node_to_push)
                self.left_node_to_push = self.left_node_to_push.left
            else:
                self.left_node_to_push = self.left_stack.pop()
                self.left_node = self.left_node_to_push
                self.left_node_to_push = self.left_node_to_push.right
                return
            
    def get_right_node(self):
        while self.right_stack or self.right_node_to_push:
            if self.right_node_to_push is not None:
                self.right_stack.append(self.right_node_to_push)
                self.right_node_to_push = self.right_node_to_push.right
            else:
                self.right_node_to_push = self.right_stack.pop()
                self.right_node = self.right_node_to_push
                self.right_node_to_push = self.right_node_to_push.left
                return
