'''
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
'''

# My solution, using 2 pointers.
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        prev_val = None
        while fast:
            curr_val = fast.val
            # We cannot simply use "if not prev_val" as the condition, because prev_val is an integer
            # and can be 0, resulting in unexpected errors.
            if prev_val is None:
                prev_val = curr_val
            elif curr_val != prev_val:
                slow.next = fast
                slow = slow.next
                prev_val = curr_val            
            fast = fast.next
            # When fast is not None, this assignment will be overwritten by subsequent iterations of
            # the while loop, so it's kinda redundant. But if we want to be precise and add a condition of 
            # "if fast is None", the code logic becomes more complicated, while a 1-liner is more concise.
            # Without this line, a list of [1, 1, 2, 3, 3] will return [1, 2, 3, 3], not the correct [1, 2, 3].                        
            slow.next = None            
        return head
      
    # A slight variation of the solution above. Now we take the assignment operation slow.next = None out of
    # the while loop, making its intention clearer.
    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        prev_val = None
        while fast:
            curr_val = fast.val
            if prev_val is None:
                prev_val = curr_val
            elif curr_val != prev_val:
                slow.next = fast
                slow = slow.next
                prev_val = curr_val            
            fast = fast.next            
        if slow:
            slow.next = None           
        return head
      
        
# Solution from https://labuladong.github.io/algo/di-ling-zh-bfe1b/shuang-zhi-fa4bd/. Simpler than my own solution,
# because it now considers separately the case where head is None, and it uses slow.val directly, rather than using
# a variable curr_val to record the value of the slow pointer.
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        fast, slow = head, head
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next            
            fast = fast.next
        slow.next = None           
        return head
    
