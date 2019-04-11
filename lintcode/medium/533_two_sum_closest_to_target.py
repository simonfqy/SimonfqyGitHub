'''
Link: https://www.lintcode.com/problem/two-sum-closest-to-target/description
'''

# My own solution.
import math
class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        if len(nums) < 2:
            return None
        min_diff = math.inf
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            summ = nums[left] + nums[right]
            abs_diff = abs(target - summ)
            if abs_diff == 0:
                return abs_diff
            if abs_diff < min_diff:
                min_diff = abs_diff
            if summ < target:
                left += 1
            else:
                right -= 1
        return min_diff
