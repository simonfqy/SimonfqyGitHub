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
