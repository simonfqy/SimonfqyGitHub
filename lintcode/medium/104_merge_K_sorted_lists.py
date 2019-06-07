"""
Link: https://www.lintcode.com/problem/merge-k-sorted-lists/description
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

# Uses priority queue. This solution is based on the one given in jiuzhang.com.
import heapq

# We need to overwrite the __lt__ function of ListNode for heapq to work.
ListNode.__lt__ = lambda x, y: (x.val < y.val) 
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if lists is None or len(lists) <= 0:
            return None
        p_queue = []
        head = None
        for node in lists:
            if node is None:
                continue
            heapq.heappush(p_queue, node)            
        
        while len(p_queue) > 0:
            node = heapq.heappop(p_queue)
            if head is None:
                head = node
                last_node = node
            else:
                last_node.next = node
                last_node = last_node.next
            if node.next is not None:
                heapq.heappush(p_queue, node.next)
                
        return head
    
    
# Merge sort, top-down.
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if lists is None or len(lists) <= 0:
            return None
        m = len(lists)
        if m == 1:
            return lists[0]
        left_head = self.mergeKLists(lists[:m//2])
        right_head = self.mergeKLists(lists[m//2:])
        return self.merge_two_sorted_linked_lists(left_head, right_head)
        
    def merge_two_sorted_linked_lists(self, left_head, right_head):
        head, last_node = None, None
        while left_head is not None and right_head is not None:
            if head is None:
                if left_head.val <= right_head.val:
                    head = left_head
                    left_head = left_head.next
                else:
                    head = right_head
                    right_head = right_head.next
                last_node = head
                continue
            
            if left_head.val <= right_head.val:
                last_node.next = left_head
                left_head = left_head.next
            else:
                last_node.next = right_head
                right_head = right_head.next
            last_node = last_node.next
            
        while left_head is None and right_head is not None:
            if head is None:
                head = right_head
                right_head = right_head.next
                last_node = head
                continue
            last_node.next = right_head
            right_head = right_head.next
            last_node = last_node.next
            
        while right_head is None and left_head is not None:
            if head is None:
                head = left_head
                left_head = left_head.next
                last_node = head
                continue
            last_node.next = left_head
            left_head = left_head.next
            last_node = last_node.next
            
        return head
    
    
# Bottom-up iterative approach.    
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if lists is None or len(lists) <= 0:
            return None
        while len(lists) > 1:
            new_lists = []
            for i in range(0, len(lists), 2):
                if i < len(lists) - 1:
                    head = self.merge_two_sorted_linked_lists(lists[i], lists[i + 1])
                else:
                    head = lists[i]
                new_lists.append(head)
            lists = new_lists
        return lists[0]
                
    # Identical to the function of the same name in the previous solution, so omitted here.
    def merge_two_sorted_linked_lists(self, left_head, right_head):
        pass
