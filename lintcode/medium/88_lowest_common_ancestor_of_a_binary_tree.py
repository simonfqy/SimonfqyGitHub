"""
Link: https://www.lintcode.com/problem/lowest-common-ancestor-of-a-binary-tree/description
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# This is my own solution using recursion. Not very concise.
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the lowest common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        self.path = []
        self.get_path(root, A)
        path_A = list(self.path)
        self.path = []
        self.get_path(root, B)
        lca_candidate = root
        for i in range(min(len(path_A), len(self.path))):
            if path_A[i] == self.path[i]:
                lca_candidate = path_A[i]
            else:
                break
        return lca_candidate
            
    def get_path(self, root, target):
        if root is None:
            return False
        while len(self.path) > 0:
            last_node = self.path[-1]
            if last_node.left != root and last_node.right != root:
                self.path.pop()
            else:
                # We must always remember to prevent the infinite loop from occurring. I only added this else clause after hitting the 
                # error many times.
                break
        self.path.append(root)
        if root.val == target.val:
            return True
        if (self.get_path(root.left, target)):
            return True
        return self.get_path(root.right, target)
    
# The iterative version corresponding to the recursive solution. Slightly better but takes more time.
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the lowest common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        path_A = self.get_path(root, A)
        path_B = self.get_path(root, B)
        lca_candidate = root
        for i in range(min(len(path_A), len(path_B))):
            if path_A[i] == path_B[i]:
                lca_candidate = path_A[i]
            else:
                break
        return lca_candidate
            
    def get_path(self, root, target):
        path = []
        if root is None:
            return path
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            while len(path) > 0:
                last_node = path[-1]
                if last_node.left != node and last_node.right != node:
                    path.pop()
                else:
                    # We must always remember to prevent the infinite loop from occurring. I only added this else clause after hitting
                    # the error many times.
                    break
            path.append(node)
            if node.val == target.val:
                return path
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
             
# A solution from jiuzhang.com provided by students. It uses recursion to get the path.
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the lowest common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        path_A = self.get_path(root, A)
        path_B = self.get_path(root, B)
        lca_candidate = None
        while path_A and path_B and path_A[-1] == path_B[-1]:
            lca_candidate = path_A.pop()
            path_B.pop()
        return lca_candidate
    
    # This is also divide-and-conquer.
    def get_path(self, root, target):
        if root is None:
            return None
        if root == target:
            return [root]
        # I did not think of this recursive method to get the path. This path is bottom-up.
        # Need to remember this way of problem-solving.
        left = self.get_path(root.left, target)
        if left:
            left.append(root)
            return left
        right = self.get_path(root.right, target)
        if right:
            right.append(root)
            return right
               
            
# Solution from jiuzhang.com. Much shorter and more elegant than my solution.            
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the lowest common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        
        # I did not realize that formulating this function as a recursive function is possible. Next time when solving 
        # tree related questions, I need to first think of possible divide-and-conquer solutions and solve it recursively.
        if root is None:
            return None
        # This if clause is quite important.
        if root == A or root == B:
            return root
        # This lca candidate (whether in left or right) can be either A or B, or the lowest common ancestor of A and B.
        # I did not realize it could be formulated like this.
        lca_candidate_in_left = self.lowestCommonAncestor(root.left, A, B)
        lca_candidate_in_right = self.lowestCommonAncestor(root.right, A, B)
        
        if lca_candidate_in_left and lca_candidate_in_right:
            return root
        if lca_candidate_in_left:
            return lca_candidate_in_left
        if lca_candidate_in_right:
            return lca_candidate_in_right
 

# My own solution in 2021.       
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the lowest common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        lca, _, _ = self.get_lca(root, A, B)
        return lca
        
    # return: lca, have_A, have_B
    def get_lca(self, root, A, B):
        if not root:
            return None, False, False
        left_lca, left_has_a, left_has_b = self.get_lca(root.left, A, B)
        right_lca, right_has_a, right_has_b = self.get_lca(root.right, A, B)
        if left_lca:
            return left_lca, left_has_a, left_has_b
        if right_lca:
            return right_lca, right_has_a, right_has_b
        have_a = left_has_a or right_has_a or root == A
        have_b = left_has_b or right_has_b or root == B
        if have_a and have_b:
            return root, True, True
        return None, have_a, have_b
    
# Similar to the solution above, but using a global variable to store lca. Now the recursive function only returns 2 values. More concise.    
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the lowest common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        self.lca = None
        self.get_lca(root, A, B)
        return self.lca
        
    # return: have_A, have_B
    def get_lca(self, root, A, B):
        if not root:
            return False, False
        left_has_a, left_has_b = self.get_lca(root.left, A, B)
        right_has_a, right_has_b = self.get_lca(root.right, A, B)
        have_a = left_has_a or right_has_a or root == A
        have_b = left_has_b or right_has_b or root == B
        if have_a and have_b and not self.lca:
            self.lca = root
        return have_a, have_b
    
# Also my own solution. This one is similar to the one provided by Jiuzhang student above.    
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the lowest common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        path_to_a = []
        path_to_b = []
        path_to_a = self.populate_path_to_node(root, path_to_a, A)
        path_to_b = self.populate_path_to_node(root, path_to_b, B)
        max_common_path_length = min(len(path_to_a), len(path_to_b))
        for i in range(max_common_path_length):
            if path_to_a[i] != path_to_b[i]:
                return path_to_a[i - 1]
        return path_to_a[max_common_path_length - 1]
    
    def populate_path_to_node(self, root, path, goal):
        if not root:
            return path
        result_path = list(path)
        result_path.append(root)
        if root is goal:
            return result_path
        left_path = self.populate_path_to_node(root.left, result_path, goal)
        if goal == left_path[-1]:
            return left_path
        right_path = self.populate_path_to_node(root.right, result_path, goal)
        if goal == right_path[-1]:
            return right_path
        return path
