'''
Link: https://www.lintcode.com/problem/middle-of-linked-list/description
'''

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

# My own solution. Traversing the linked list twice.
class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        # write your code here
        current = head
        number = 0
        while current != None:
            number += 1
            current = current.next
        mid = (number - 1) // 2
        current = head
        number = 0
        while current != None:
            if number == mid:
                return current
            number += 1
            current = current.next
            
            
# My solution based on the hint given in Jiuzhang.com.            
class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        # write your code here
        fast = head
        slow = head
        number = 0
        while fast != None and fast.next != None:
            fast = fast.next
            number += 1
            if number % 2 == 0:
                slow = slow.next
            
        return slow
    

# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

class Solution:
    # @param head: the head of linked list.
    # @return: a middle node of the linked list
    def middleNode(self, head):
        # Write your code here
        if head is None:
            return None
        slow = head
        fast = slow.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow
