"""
https://www.lintcode.com/problem/binary-tree-level-order-traversal/description
My solution is using level order BFS traversal.
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        queue = deque()
        ret_list = []
        if root is None:
            return ret_list
        queue.append(root)
        while queue:
            size = len(queue)
            this_level_elements = []
            for _ in range(size):
                head = queue.popleft()                
                this_level_elements.append(head.val)
                if head.left is not None:
                    queue.append(head.left)
                if head.right is not None:
                    queue.append(head.right)
            ret_list.append(this_level_elements)
        return ret_list

    
# This solution is based on the teachings from Jiuzhang.com. Uses 2 queues.
from collections import deque
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        output_list = []
        if root is None:
            return output_list
        queue1 = deque()
        queue2 = deque()
        queue1.append(root)
        while queue1:
            this_level_nodes = []
            for _ in range(len(queue1)):
                node = queue1.popleft()
                if node.left is not None:
                    queue2.append(node.left)
                if node.right is not None:
                    queue2.append(node.right)
                this_level_nodes.append(node.val)
            queue1, queue2 = queue2, queue1
            output_list.append(this_level_nodes)
        return output_list
    
    
# Conceptually similar to the last one.    
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        if not root:
            return []

        queue = [root]
        results = []
        while queue:
            next_queue = []
            results.append([node.val for node in queue])
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        return results
