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
