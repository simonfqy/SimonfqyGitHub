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
        prefix_sum = 0
        smallest = 0
        maximum = None
        for number in nums:
            prefix_sum += number
            if maximum is None:
                maximum = prefix_sum
            else:
                maximum = max(maximum, prefix_sum - smallest)
            smallest = min(smallest, prefix_sum)
        return maximum
