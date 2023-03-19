'''
Link: https://www.lintcode.com/problem/96/
'''

# My own solution. 
"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head: ListNode, x: int) -> ListNode:
        smaller_list = ListNode(None)
        larger_list = ListNode(None)
        smaller_cursor = smaller_list
        larger_cursor = larger_list
        cursor = head

        while cursor:
            if cursor.val < x:
                smaller_cursor.next = cursor
                smaller_cursor = smaller_cursor.next
            else:
                larger_cursor.next = cursor
                larger_cursor = larger_cursor.next
            cursor = cursor.next
            # Make sure these two cursors' next pointers point to None. Otherwise there'll be issues.
            smaller_cursor.next = None
            larger_cursor.next = None

        smaller_cursor.next = larger_list.next

        return smaller_list.next
      
      
# Solution from https://labuladong.github.io/algo/di-ling-zh-bfe1b/shuang-zhi-0f7cc/.
# Similar to my own solution above, but the treatment of next pointers is a bit different.
class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head: ListNode, x: int) -> ListNode:
        # write your code here
        smaller_list = ListNode(None)
        larger_list = ListNode(None)
        smaller_cursor = smaller_list
        larger_cursor = larger_list
        cursor = head

        while cursor:
            if cursor.val < x:
                smaller_cursor.next = cursor
                smaller_cursor = smaller_cursor.next
            else:
                larger_cursor.next = cursor
                larger_cursor = larger_cursor.next
            # Breaks the linkage, purpose is similar to the solution above but implementation is different.
            # This implementation is more efficient but less understandable.
            temp = cursor.next
            cursor.next = None
            cursor = temp

        smaller_cursor.next = larger_list.next

        return smaller_list.next      
