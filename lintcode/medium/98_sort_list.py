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

    
# My implementation based on a solution from Jiuzhang.com. Uses quicksort, but partitions the list into 3 sections.      
class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sort_list(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy_l, dummy_m, dummy_r = ListNode(-1), ListNode(-1), ListNode(-1)
        tail_l, tail_m, tail_r = dummy_l, dummy_m, dummy_r
        mid_node = self.find_mid(head)
        pivot = mid_node.val
        temp = head
        while temp:
            if temp.val < pivot:
                tail_l.next = temp
                tail_l = tail_l.next
            elif temp.val == pivot:
                tail_m.next = temp
                tail_m = tail_m.next
            else:
                tail_r.next = temp
                tail_r = tail_r.next
            temp = temp.next
        tail_l.next, tail_m.next, tail_r.next = None, None, None
        left = self.sort_list(dummy_l.next)
        right = self.sort_list(dummy_r.next)
        return self.concat(left, dummy_m.next, right)

    
    def find_mid(self, head):
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def concat(self, left, mid, right):
        dummy = ListNode(-1, left)
        curr = dummy
        while curr.next:
            curr = curr.next
        curr.next = mid
        while curr.next:
            curr = curr.next
        curr.next = right
        return dummy.next
    
