'''
Link: https://www.lintcode.com/problem/two-sum-greater-than-target/description
'''

# My solution.
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        count = 0
        if len(nums) < 2:
            return count
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                count += right - left
                right -= 1
            else:
                left += 1
        return count
