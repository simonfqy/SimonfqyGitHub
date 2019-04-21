'''
Link: https://www.lintcode.com/problem/move-zeroes/description
'''

# My own solution.
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        if nums is None or len(nums) <= 1:
            return
        left, right = 0, 1
        while right < len(nums):
            while right < len(nums) and nums[left] != 0:
                left += 1
                right += 1
            while right < len(nums) and nums[right] == 0:
                right += 1
            if right < len(nums):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
        return
