'''
Link: https://www.lintcode.com/problem/recover-rotated-sorted-array/description
'''

# This is my own solution based on the teachings in Jiuzhang.com. It is sorting in-place.
class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if not len(nums):
            return
        ind_smallest_ele = 0
        smallest_ele = nums[0]
        for i, num in enumerate(nums):
            if num < smallest_ele:
                ind_smallest_ele = i
                smallest_ele = num
        
        self.reverse(nums, 0, ind_smallest_ele - 1)
        self.reverse(nums, ind_smallest_ele, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)
        
        
    def reverse(self, nums, start, end):
        while start < end:
            left_ele = nums[start]
            nums[start] = nums[end]
            nums[end] = left_ele
            start += 1
            end -= 1
