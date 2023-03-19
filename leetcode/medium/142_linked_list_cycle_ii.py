'''
Link: https://leetcode.com/problems/linked-list-cycle-ii/description/
A variant of this question was asked in Shakudo's second round technical interview in Mar 2023. 
I was unable to solve it.
'''

# My solution based on https://labuladong.github.io/algo/di-ling-zh-bfe1b/shuang-zhi-0f7cc/.
# Uses two pointers, has O(1) space complexity.
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        has_cycle = False    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # Assume slow pointer moved k steps to reach this node, while the fast pointer moved 2k steps. Hence,
            # k is a multiple of the cycle length, such that cycle length * c = k, where c is a positive integer.
            if slow == fast:
                has_cycle = True
                break
        if not has_cycle:
            return None
        # We're now searching for the starting position of the cycle.
        # Assume that the position of fast pointer is m length away from the beginning of the cycle, and we know that
        # it is k length away from the head, so the beginning of the cycle is k - m length away from the head. When another
        # pointer is moving along the cycle from the current position, after moving for k - m steps, we have moved 
        # m + k - m = k steps from the beginning of the cycle, which goes right back to the beginning of the cycle. And at 
        # the same moment, the slow pointer has moved k - m length from the head, hence the two pointers now meet at the 
        # beginning of the cycle.
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
      
      
