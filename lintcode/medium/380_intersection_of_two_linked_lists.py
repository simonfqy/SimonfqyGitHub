'''
Link: https://www.lintcode.com/problem/intersection-of-two-linked-lists/description
'''

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

# I wrote this solution by myself. It uses set() hence it uses O(n) extra memory, not optimal.
class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        if headA is None or headB is None:
            return None
        a_ptr, b_ptr = headA, headB
        visited = set()
        while a_ptr is not None or b_ptr is not None:
            if a_ptr is not None:
                if a_ptr in visited:
                    return a_ptr
                visited.add(a_ptr)
                a_ptr = a_ptr.next
            if b_ptr is not None:
                if b_ptr in visited:
                    return b_ptr
                visited.add(b_ptr)
                b_ptr = b_ptr.next
        return None

 
# This solution is based on a hint in the discussion section. Although it works correctly,
# its problem is that the time limit is easily exceeded.
class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        if headA is None or headB is None:
            return None
        a_ptr, b_ptr = headA, headB
        len_a, len_b = 0, 0
        a_cycle, b_cycle = 0, 0
        while True:
            if a_ptr.val == b_ptr.val:
                return a_ptr
            if a_cycle == 0:
                len_a += 1
            if b_cycle == 0:
                len_b += 1
            if a_ptr.next is not None:
                a_ptr = a_ptr.next
            else:
                a_ptr = headA
                a_cycle += 1
                if b_cycle >= 1 and (a_cycle * len_a) % len_b == 0:
                    return None
            
            if b_ptr.next is not None:
                b_ptr = b_ptr.next
            else:
                b_ptr = headB
                b_cycle += 1
                if a_cycle >= 1 and (b_cycle * len_b) % len_a == 0:
                    return None
        return None
    

# Based on the solution from Jiuzhang.com. Traverses the linked list twice.
class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        if headA is None or headB is None:
            return None
        a_ptr, b_ptr = headA, headB
        len_a, len_b = 1, 1
        
        while a_ptr.next is not None:
            a_ptr = a_ptr.next
            len_a += 1
        while b_ptr.next is not None:
            b_ptr = b_ptr.next
            len_b += 1
        
        a_ptr, b_ptr = headA, headB
        while len_a > 0 and len_b > 0:
            if a_ptr.val == b_ptr.val:
                return a_ptr
            
            if len_b > len_a:
                b_ptr = b_ptr.next
                len_b -= 1
            elif len_b < len_a:
                a_ptr = a_ptr.next
                len_a -= 1
            else:
                a_ptr = a_ptr.next
                b_ptr = b_ptr.next
                len_a -= 1
                len_b -= 1
                
        return None
    
    
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        # Write your code here
        lenA, lenB = 0, 0
        node1, node2 = headA, headB
        while node1 is not None:
            lenA += 1
            node1 = node1.next
        while node2 is not None:
            lenB += 1
            node2 = node2.next
        
        node1, node2 = headA, headB
        while lenA > lenB:
            node1 = node1.next
            lenA -= 1
        while lenB > lenA:
            node2 = node2.next
            lenB -=1
        while node1 is not node2:
            node1 = node1.next
            node2 = node2.next
        return node1    
