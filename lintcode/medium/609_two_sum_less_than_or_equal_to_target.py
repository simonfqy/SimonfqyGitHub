'''
Link: https://www.lintcode.com/problem/two-sum-less-than-or-equal-to-target/description
Similar to the 382. triangle count problem.
'''

# My own solution.
class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        count = 0
        if not nums or len(nums) < 2:
            return count
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] <= target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count
