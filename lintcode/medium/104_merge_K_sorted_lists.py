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
            
        if left_head is None and right_head is not None:
            if head is None:
                head = right_head
            else:
                last_node.next = right_head
            
        if right_head is None and left_head is not None:
            if head is None:
                head = left_head
            else:
                last_node.next = left_head
            
        return head
    
    
    
# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        return self.merge_range_lists(lists, 0, len(lists) - 1)
        
    def merge_range_lists(self, lists, start, end):
        if start == end:
            return lists[start]
        
        mid = (start + end) // 2
        left = self.merge_range_lists(lists, start, mid)
        right = self.merge_range_lists(lists, mid + 1, end)
        return self.merge_two_lists(left, right)
        
    # This way of merging using dummy node is more succinct than my code.
    def merge_two_lists(self, head1, head2):
        tail = dummy = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
            
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
        
        return dummy.next
    
    
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
