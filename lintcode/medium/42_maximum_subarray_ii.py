'''
Link: https://www.lintcode.com/problem/42
'''


# My own solution. It is directly from the solution for question 45:
# https://github.com/simonfqy/SimonfqyGitHub/blob/6f70a9737255b06bb8192fad8db618de6c60426a/lintcode/medium/45_maximum_subarray_difference.py#L9
class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        if not nums or len(nums) <= 1:
            return 0
        n = len(nums)
        left_max_sum, right_max_sum = [0] * n, [0] * n
        min_sum, prefix_sum = 0, 0
        max_sum = float('-inf')
        for i in range(n):
            prefix_sum += nums[i]
            max_sum = max(max_sum, prefix_sum - min_sum)
            left_max_sum[i] = max_sum
            min_sum = min(min_sum, prefix_sum)
        min_sum, right_side_sum = 0, 0
        max_sum = float('-inf')
        for j in range(n - 1, -1, -1):
            right_side_sum += nums[j]
            max_sum = max(max_sum, right_side_sum - min_sum)
            right_max_sum[j] = max_sum
            min_sum = min(min_sum, right_side_sum)
        max_subarrays_sum = float('-inf')
        for i in range(n - 1):
            max_subarrays_sum = max(max_subarrays_sum, left_max_sum[i] + right_max_sum[i + 1])
        return max_subarrays_sum
        
