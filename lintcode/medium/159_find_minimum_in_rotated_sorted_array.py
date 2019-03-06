'''
Link: https://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array/description
'''

# I wrote this solution.
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        first_num = nums[0]
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if (nums[mid] > first_num):
                start = mid
            else:
                end = mid
        return min(first_num, nums[start], nums[end])
