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
