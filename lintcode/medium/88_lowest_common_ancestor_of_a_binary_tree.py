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
