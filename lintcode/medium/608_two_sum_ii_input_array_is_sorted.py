'''
Link: https://www.lintcode.com/problem/two-sum-ii-input-array-is-sorted/description
'''

# It is fairly easy.
class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        left, right = 0, len(nums) - 1
        while left < right:
            num_sum = nums[left] + nums[right]
            if num_sum == target:
                return [left + 1, right + 1]
            if num_sum < target:
                left += 1
            else:
                right -= 1
