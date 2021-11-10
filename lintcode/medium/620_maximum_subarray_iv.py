'''
https://www.lintcode.com/problem/620
'''

# My own solution. Uses 2 pointer, but still has O(n^2) time complexity.
class Solution:
    """
    @param nums: an array of integer
    @param k: an integer
    @return: the largest sum
    """
    def maxSubarray4(self, nums, k):
        if not nums or len(nums) < k:
            return 0
        n = len(nums)
        prefix_sum = 0
        prefix_sum_list = [0]
        for num in nums:
            prefix_sum += num
            prefix_sum_list.append(prefix_sum)
        min_sum = float('inf')
        max_subarray_sum = prefix_sum_list[k]
        start = 1
        while start < n - k + 2:
            if prefix_sum_list[start - 1] >= min_sum:
                start += 1
                continue
            min_sum = prefix_sum_list[start - 1]
            end = start + k - 1
            while end < n + 1:
                latest_possible_start_ind = end - k + 1                
                min_sum = min(min_sum, prefix_sum_list[latest_possible_start_ind - 1])
                max_subarray_sum = max(max_subarray_sum, prefix_sum_list[end] - min_sum)
                end += 1
            start += 1

        return max_subarray_sum
