'''
Link: https://www.lintcode.com/problem/linked-list-cycle-ii/description
'''

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

# My own solution which uses set.
class Solution:
    """
    @param head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if head is None:
            return None
        node_set = set()
        node = head
        while node is not None:
            if node in node_set:
                return node
            node_set.add(node)
            node = node.next
        return None
    

# Based on the teaching from Jiuzhang.com. Get the convergence point of the fast and slow pointers,
# where the fast pointer traverses 2 steps at a time and slow pointer 1 at a time. Then, after finding
# the convergence point, designate 1 pointer starting from the head node, another pointer starting from
# the convergence point, and return the node in which they meet. It can be proved mathematically.
class Solution:
    """
    @param head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if head is None:
            return None
        convergence = self.get_convergence(head)
        if convergence is None:
            return None
        node_1, node_2 = head, convergence
        while True:
            if node_1 == node_2:
                return node_1
            node_1 = node_1.next
            node_2 = node_2.next
                
        return None
        
    def get_convergence(self, head):
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None

    
    
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


from lintcode import ListNode

class Solution:
    """
    @param head: The first node of the linked list.
    @return: the node where the cycle begins. 
                If there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if head == None or head.next == None:
            return None
        slow = fast = head      	#初始化快指针和慢指针
        while fast and fast.next:	
            slow = slow.next
            fast = fast.next.next
            if fast == slow:		#快慢指针相遇
                break
        if slow == fast:
            slow = head				#从头移动慢指针
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow				#两指针相遇处即为环的入口
        return None
