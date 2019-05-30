'''
Link: https://www.lintcode.com/problem/next-permutation-ii/description
'''

# Not much difference from problem 52.
class Solution:
    """
    @param nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):
        # write your code here
        ind_start_reverse = -1
        for i in range(len(nums) - 1, -1, -1):
            if i > 0 and nums[i] <= nums[i - 1]:
                continue
            ind_start_reverse = i
            break
        if ind_start_reverse > 0:
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] > nums[ind_start_reverse - 1]:
                    nums[i], nums[ind_start_reverse - 1] = nums[ind_start_reverse - 1], nums[i]
                    break
        self.reverse(nums, ind_start_reverse, len(nums) - 1)
        return
            
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
