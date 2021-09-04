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
    
    
# This answer is obtained from jiuzhang.com, with only slight modification. It is very similar to the solution above. 
# It first gets all the values using in-order traversal, then gets the index of the largest value smaller than or equal to
# the target in the list using binary search, then it uses two pointers to find the desired K values.
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        all_values = self.get_value_list(root)
        left = self.get_ind_of_closest_smaller_value(all_values, target)
        right = left + 1
        closest_k_values = []
        for _ in range (k):
            if self.is_left_closer(all_values, left, right, target):
                closest_k_values.append(all_values[left])
                left -= 1
            else:
                closest_k_values.append(all_values[right])
                right += 1

        return closest_k_values

    def get_value_list(self, root):     
        dummy = TreeNode(0)
        dummy.right = root 
        stack = [dummy]  
        value_list = []
        while stack:
            node = stack.pop()
            if node.right:
                n = node.right
                while n:
                    stack.append(n)
                    n = n.left
            if stack:
                value_list.append(stack[-1].val)
        return value_list

    # Use binary search to find the index of the index of the largest element smaller than or equal to the target 
    def get_ind_of_closest_smaller_value(self, all_values, target):
        left, right = 0, len(all_values) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if all_values[mid] <= target:
                left = mid
            else:
                right = mid
        if all_values[right] <= target:
            return right
        if all_values[left] <= target:
            return left
        return -1

    def is_left_closer(self, value_list, left, right, target):
        if right >= len(value_list):
            return True
        if left < 0:
            return False
        return abs(value_list[left] - target) <= abs(value_list[right] - target)
    
    
# It uses the inorder traversal, left & right direction. In idea it is similar to my first solution,
# but this one takes less time.
# Refer to: 
# https://github.com/simonfqy/SimonfqyGitHub/blob/e8ae2c5a485cb63d456a03916f77c035d3cc58ed/lintcode/hard/86_binary_search_tree_iterator.py#L75
# Note that the solution in the following link does not work in our case:
# https://github.com/simonfqy/SimonfqyGitHub/blob/9930808eb6869a94cb68b52d7c120bef623e41eb/algorithms/DFS_and_different_traversals.py#L77
# 相当于在 bst 里get next node & get previous node
# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        if root is None or k == 0:
            return []
            
        lower_stack = self.get_stack(root, target)
        upper_stack = list(lower_stack)
        if lower_stack[-1].val < target:
            self.move_upper(upper_stack)
        else:
            self.move_lower(lower_stack)
        
        result = []
        for i in range(k):
            if self.is_lower_closer(lower_stack, upper_stack, target):
                # The lower_stack and upper_stack will only have its last element being appended to the answer
                # at any given time.
                result.append(lower_stack[-1].val)
                self.move_lower(lower_stack)
            else:
                result.append(upper_stack[-1].val)
                self.move_upper(upper_stack)
                
        return result
        
    def get_stack(self, root, target):
        stack = []
        while root:
            stack.append(root)
            if target < root.val:
                root = root.left
            else:
                root = root.right
                
        return stack
    
    # This traversal is the same as the implementation in:  
    # https://github.com/simonfqy/SimonfqyGitHub/blob/e8ae2c5a485cb63d456a03916f77c035d3cc58ed/lintcode/hard/86_binary_search_tree_iterator.py#L75
    def move_upper(self, stack):
        # We want to modify stack here, such that its last element will always be the upper neighbor of the
        # last element of the stack before move_upper() is called each time.
        # Be aware of the conditions.
        if stack[-1].right:
            node = stack[-1].right
            while node:
                stack.append(node)
                node = node.left
        else:
            node = stack.pop()
            # Some elements in the stack are actually already traversed (they have been added to the answer
            # list when they are the last element of lower_stack or upper_stack). For those we simply use
            # a while loop to pop them out without returning to the main function.
            while stack and stack[-1].right == node:
                node = stack.pop()
                
    def move_lower(self, stack):
        if stack[-1].left:
            node = stack[-1].left
            while node:
                stack.append(node)
                node = node.right
        else:
            node = stack.pop()
            while stack and stack[-1].left == node:
                node = stack.pop()
                
    def is_lower_closer(self, lower_stack, upper_stack, target):
        if not lower_stack:
            return False
            
        if not upper_stack:
            return True
            
        return target - lower_stack[-1].val < upper_stack[-1].val - target
    
    
# My own solution after slightly borrowing from jiuzhang.com. It is not a very recommended solution, because the time complexity is O(n).
# It is using two pointers, one forward pointer starting from beginning, one backward pointer starting from the end.
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        self.upper_stack, self.lower_stack = [], []
        all_values = []
        next_node, prev_node = self.get_first_node(root), self.get_last_node(root) 
        while prev_node and prev_node.val >= target:
            prev_node = self.get_previous_node()
        while next_node and next_node.val < target:
            next_node = self.get_next_node()
        while len(all_values) < k:
            if prev_node and (not next_node or abs(prev_node.val - target) <= abs(next_node.val - target)):             
                all_values.append(prev_node.val)                
                prev_node = self.get_previous_node()
            else:
                all_values.append(next_node.val)
                next_node = self.get_next_node()
        return all_values 

    # If we simply initialize the upper and lower stacks following the get_stack() function in the solution above,
    # it will not work correctly. That is because the traversal is implemented differently here, using a dummy node as
    # in https://github.com/simonfqy/SimonfqyGitHub/blob/9930808eb6869a94cb68b52d7c120bef623e41eb/algorithms/DFS_and_different_traversals.py#L77.
    # The get_stack() function in the solution above only works for the traversal method in 
    # https://github.com/simonfqy/SimonfqyGitHub/blob/e8ae2c5a485cb63d456a03916f77c035d3cc58ed/lintcode/hard/86_binary_search_tree_iterator.py#L75
    
    def get_first_node(self, root):
        while root:
            self.upper_stack.append(root)
            root = root.left
        return self.upper_stack[-1]

    def get_last_node(self, root):
        while root:        
            self.lower_stack.append(root)
            root = root.right
        return self.lower_stack[-1]     

    # return the next value in in-order traversal
    def get_next_node(self):
        node = self.upper_stack.pop()
        if node.right:
            node = node.right
            while node:
                self.upper_stack.append(node)                
                node = node.left
        if not self.upper_stack:
            return None
        return self.upper_stack[-1]

    def get_previous_node(self):
        node = self.lower_stack.pop()
        if node.left:
            node = node.left
            while node:
                self.lower_stack.append(node)
                node = node.right
        if not self.lower_stack:
            return None
        return self.lower_stack[-1]
