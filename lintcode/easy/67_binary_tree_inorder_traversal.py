'''
https://www.lintcode.com/problem/binary-tree-inorder-traversal/description
Can refer to this: 
https://github.com/simonfqy/SimonfqyGitHub/blob/c6111760e973df45c8291bc739198db9120063f5/algorithms/DFS_and_different_traversals.py#L61
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# The iterative version. Done by myself.
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        output_list = []
        if root is None:
            return output_list
        stack = []
        node = root
        while stack or node:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                output_list.append(node.val)
                node = node.right
            
        return output_list
    
    
# 本参考程序来自九章算法，由 @社会我喵哥 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


"""
九章标准答案iterate java版本的python 翻译

挪到下一个点的算法如下:
• 如果当前点存在右子树，那么就是右子树中“一路向西”最左边的那个点
• 如果当前点不存在右子树，则是走到当前点的路径中，第一个左拐的点
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        stack = []
        result = []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node = stack[-1]
            result.append(node.val)
            if node.right: 
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            else:
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()
        return result
