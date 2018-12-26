"""
Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Please also refer to https://github.com/simonfqy/SimonfqyGitHub/blob/d8075bd4a1f3fc122daafd05684e98cfa2071da3/leetcode/algorithms/DFS_and_different_traversals.py#L78
"""

# I did not use the single-stack version. That one is too complicated.
class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret_list = []
        s1 = [root]
        s2 = []
        if root is None:
            return ret_list
        while s1:
            node = s1.pop()
            s2.append(node)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
            
        while s2:
            node = s2.pop()
            ret_list.append(node.val)
        return ret_list
