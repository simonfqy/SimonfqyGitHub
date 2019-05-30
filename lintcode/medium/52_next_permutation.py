'''
Link: https://www.lintcode.com/problem/next-permutation/description
'''

# Based on the teachings from Jiuzhang.com.
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        ind_start_reversal = -1
        for i in range(len(nums) - 1, -1, -1):
            if i > 0 and nums[i] <= nums[i - 1]:
                continue
            ind_start_reversal = i
            break
        if ind_start_reversal == 0:
            self.reverse_list(nums, ind_start_reversal, len(nums) - 1)
            return nums
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[ind_start_reversal - 1]:
                nums[i], nums[ind_start_reversal - 1] = nums[ind_start_reversal - 1], nums[i]
                break
        self.reverse_list(nums, ind_start_reversal, len(nums) - 1)
        return nums
        
        
    def reverse_list(self, nums, start, end):
        left, right = start, end
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
