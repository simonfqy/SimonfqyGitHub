'''
Link: https://www.lintcode.com/problem/sort-colors/description
'''

# My solution based on the teachings from Jiuzhang.com.
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if len(nums) <= 0:
            return
        left, right = 0, len(nums) - 1
        middle = 0
        while middle <= right:
            if nums[middle] == 0:
                nums[left], nums[middle] = nums[middle], nums[left]
                left += 1
                middle += 1
            elif nums[middle] == 2:
                nums[right], nums[middle] = nums[middle], nums[right]
                right -= 1
            else:
                middle += 1
        return
