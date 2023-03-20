'''
Link: https://leetcode.com/problems/remove-element/description/
'''

# My own solution. Uses 2 pointers: a fast one and a slow one.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            if i != slow:
                nums[i], nums[slow] = nums[slow], nums[i]
            slow += 1
        return slow
      
      
