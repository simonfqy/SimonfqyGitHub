'''
Link: https://www.lintcode.com/problem/partition-array/description
'''

# My own solution
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if len(nums) <= 0:
            return 0
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] < k:
                left += 1
            while left < right and k <= nums[right]:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        # compare the values
        if nums[left] >= k:
            return left
        if nums[right] >= k:
            return right
        return right + 1
