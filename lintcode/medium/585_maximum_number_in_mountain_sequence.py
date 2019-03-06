'''
https://www.lintcode.com/problem/maximum-number-in-mountain-sequence/description
'''

# This is my own solution.
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if nums is None or not len(nums):
            return -1
        first_num = nums[0]
        if len(nums) == 1:
            return first_num
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if mid <= 0:
                break
            if nums[mid] - nums[mid - 1] < 0:
                end = mid
            else:
                start = mid
        return max(nums[start], nums[end]) 
