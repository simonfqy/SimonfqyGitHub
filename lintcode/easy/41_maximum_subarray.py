'''
Link: https://www.lintcode.com/problem/maximum-subarray/description
'''

# My own solution 2 months after watching jiuzhang.com videos. Uses prefix sum Dynamic Programming. 
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if nums is None or len(nums) <= 0:
            return None
        prefix_sums = [0 for _ in nums]
        smallest = 0
        largest_gap = None
        for i, number in enumerate(nums):
            if i == 0:
                prefix_sums[i] = number
            else:
                prefix_sums[i] = number + prefix_sums[i - 1]
            if largest_gap is None or largest_gap < prefix_sums[i] - smallest:
                largest_gap = prefix_sums[i] - smallest
            if smallest > prefix_sums[i]:
                smallest = prefix_sums[i]
        return largest_gap
