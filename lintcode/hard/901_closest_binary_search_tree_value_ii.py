'''
Link: https://www.lintcode.com/problem/closest-binary-search-tree-value-ii/description
'''

# This solution does not work, because it causes "time limit exceeded" problem.
# The idea is a two pointer algorithm applied to BST.
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        self.left_stack, self.right_stack = [], []
        self.left_node_pointer, self.right_node_pointer = root, root
        self.get_closest_pair(root, target)
        self.left_node_to_push, self.right_node_to_push = self.left_node_pointer.left, self.right_node_pointer.right
        
        value_list = []
        while len(value_list) < k:
            left_val, right_val = self.left_node_pointer.val, self.right_node_pointer.val
            if abs(left_val - target) <= abs(right_val - target):
                if left_val not in set(value_list):
                    value_list.append(left_val)
                self.move_left_pointer()
            else:
                if right_val not in set(value_list):
                    value_list.append(right_val)
                self.move_right_pointer()
        return value_list
        
    
    def get_closest_pair(self, root, target):
        while root:
            self.right_stack.append(root)
            self.left_stack.append(root)
            if root.val == target:
                # We mandate that the right_node_pointer always points to the exact
                # match should any exist.
                self.right_node_pointer = root
                break
            elif root.val > target:
                self.right_node_pointer = root
                root = root.left
            else:
                self.left_node_pointer = root
                root = root.right
        self.right_stack.pop()
        self.left_stack.pop()
        return
    
    def move_left_pointer(self):
        while self.left_stack or self.left_node_to_push:
            if self.left_node_to_push is not None:
                self.left_stack.append(self.left_node_to_push)
                self.left_node_to_push = self.left_node_to_push.right
            else:
                self.left_node_to_push = self.left_stack.pop()
                self.left_node_pointer = self.left_node_to_push
                self.left_node_to_push = self.left_node_to_push.left
                return
            
    def move_right_pointer(self):
        while self.right_stack or self.right_node_to_push:
            if self.right_node_to_push is not None:
                self.right_stack.append(self.right_node_to_push)
                self.right_node_to_push = self.right_node_to_push.left
            else:
                self.right_node_to_push = self.right_stack.pop()
                self.right_node_pointer = self.right_node_to_push
                self.right_node_to_push = self.right_node_to_push.right
                return
            
# A brute-force solution with O(n) time complexity. But it does not cause time limit exceeded problems.
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        stack = []
        node = root
        values = []
        while stack or node:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                values.append(node.val)
                node = node.right
        first_greater_pos = self.get_first_greater_pos(values, target)
        # It is fine if all of the entries are smaller than target.
        return self.get_k_values(values, first_greater_pos, target, k)
        
    def get_first_greater_pos(self, values, target):
        left, right = 0, len(values) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if values[mid] < target:
                left = mid
            else:
                right = mid
        if values[left] >= target:
            return left
        return right
        
    def get_k_values(self, values, first_greater_pos, target, k):
        left, right = first_greater_pos - 1, first_greater_pos
        closest_k_values = []
        while len(closest_k_values) < k:
            if left < 0:
                # can only advance right pointer.
                closest_k_values.append(values[right])
                right += 1
                continue
            if right >= len(values):
                closest_k_values.append(values[left])
                left -= 1
                continue
            if abs(values[left] - target) <= abs(values[right] - target):
                closest_k_values.append(values[left])
                left -= 1
            else:
                closest_k_values.append(values[right])
                right += 1
        return closest_k_values
