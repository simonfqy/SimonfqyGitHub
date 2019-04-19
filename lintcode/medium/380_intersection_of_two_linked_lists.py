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
