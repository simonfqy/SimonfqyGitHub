'''
https://www.lintcode.com/problem/45
'''


# My implementation based on the instruction from jiuzhang.com. Uses Dynamic Programming, takes O(n) time and space complexity.
# I initially did not think of using prefix sum to calculate the maximum and minimum subarrays, which turned out to be too complicated.
# Having the right mental model can simplify things a LOT.
class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    def maxDiffSubArrays(self, nums):     
        if not nums or len(nums) <= 1:
            return 0   
        max_diff = 0
        n = len(nums)
        # Left side is inclusive, right side is not.
        left_side_max_subarray_sum, left_side_min_subarray_sum = dict(), dict()
        right_side_max_subarray_sum, right_side_min_subarray_sum = dict(), dict()
        prefix_sum = 0
        min_sum, max_sum = 0, 0
        left_max, left_min = float('-inf'), float('inf')
        for i in range(n - 1):
            prefix_sum += nums[i]
            left_max = max(left_max, prefix_sum - min_sum)
            left_min = min(left_min, prefix_sum - max_sum)
            left_side_max_subarray_sum[i] = left_max
            left_side_min_subarray_sum[i] = left_min
            min_sum = min(min_sum, prefix_sum)
            max_sum = max(max_sum, prefix_sum)

        right_hand_sum = 0
        min_sum, max_sum = 0, 0
        right_max, right_min = float('-inf'), float('inf')
        for j in range(n - 2, -1, -1):
            right_hand_sum += nums[j + 1]
            right_max = max(right_max, right_hand_sum - min_sum)
            right_min = min(right_min, right_hand_sum - max_sum)
            right_side_max_subarray_sum[j] = right_max
            right_side_min_subarray_sum[j] = right_min
            min_sum = min(min_sum, right_hand_sum)
            max_sum = max(max_sum, right_hand_sum)
         
        for i in range(n - 1):
            max_diff = max(max_diff, left_side_max_subarray_sum[i] - right_side_min_subarray_sum[i], \
                    right_side_max_subarray_sum[i] - left_side_min_subarray_sum[i])
        return max_diff
