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
