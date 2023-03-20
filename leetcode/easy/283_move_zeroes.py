'''
Link: https://leetcode.com/problems/move-zeroes/description/
'''

# My own solution. Uses two pointers.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        slow = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            if i != slow:
                nums[slow], nums[i] = nums[i], nums[slow]
            slow += 1
            
            
