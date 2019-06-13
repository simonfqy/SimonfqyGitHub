"""
Link: https://www.lintcode.com/problem/binary-search-tree-iterator/description
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


# My own implementation, uses dummy node, not quite optimal.
class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        dummy = TreeNode(0)
        dummy.right = root
        self.stack = [dummy]
        self.already_got_next_one = False

    """
    @return: True if there has next node, or false
    """
    # In other implementations, the logic of hasNext() is much simpler.
    def hasNext(self):
        # write your code here
        if self.already_got_next_one:
            return True
        if self.next() is not None:
            self.already_got_next_one = True
            return True
        self.already_got_next_one = False
        return False

    """
    @return: return next node
    """
    def next(self):
        # write your code here
        if self.already_got_next_one:
            self.already_got_next_one = False
            return self.stack[-1]
            
        if len(self.stack) > 0:
            if self.stack[-1].right:
                node = self.stack[-1].right
                while node:
                    self.stack.append(node)
                    node = node.left
            else:
                node = self.stack.pop()
                while self.stack and node == self.stack[-1].right:
                    node = self.stack.pop()
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    
    
# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        self.stack = []
        # Gets rid of dummy node, populates the stack from the start.
        while root != None:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # This works. If we use this in the previous solution, it will not work.
        return len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self):
        # node is obtained at the beginning.
        node = self.stack[-1]
        if node.right is not None:
            n = node.right
            while n != None:
                self.stack.append(n)
                n = n.left
        else:
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()
        # Node obtained in the beginning is returned. Unlike my solution which returns self.stack[-1] at the
        # end, this one obtains the node at the beginning. This is because we have already populated the self.stack
        # in this implementation, while in my own solution the self.stack[] is empty when it was initialized.
        return node
    
    
# My implementation using stackoverflow's inorder traversal.
class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        self.node = root

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        return self.node or len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self):
        # write your code here
        while self.node or self.stack:
            if self.node:
                self.stack.append(self.node)
                self.node = self.node.left
            else:
                self.node = self.stack.pop()
                curt = self.node
                self.node = self.node.right
                return curt
