'''
Link: https://www.lintcode.com/problem/98/
'''

from lintcode import (
    ListNode,
)

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

# My implementation of the merge sort solution provided by jiuzhang.com. Uses 2 pointers: 1 fast, 1 slow.
class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sort_list(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        fast, slow = head, head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        list1 = self.sort_list(head)
        list2 = self.sort_list(mid)
        return self.merge(list1, list2)
        
    def merge(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        temp = head
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp.next = list1
                temp = temp.next
                list1 = list1.next
            else:
                temp.next = list2
                temp = temp.next
                list2 = list2.next
        if not list1:
            temp.next = list2
        if not list2:
            temp.next = list1 

        return head

      
