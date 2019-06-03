'''
Link: https://www.lintcode.com/problem/minimum-subarray/description
'''

# Uses prefix sum.
class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        prefix_sum = 0
        max_sum = 0
        min_sum = None
        for number in nums:
            prefix_sum += number
            if min_sum is None:
                min_sum = prefix_sum
            else:
                min_sum = min(min_sum, prefix_sum - max_sum)
            max_sum = max(max_sum, prefix_sum)
            
        return min_sum

    
# Greedy algorithm.    
class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        curr_sum = 0
        min_sum = None
        # A minimum subarray will not begin or end with a positive-sum subarray.
        for number in nums:
            curr_sum += number
            if min_sum is None:
                min_sum = curr_sum
            min_sum = min(min_sum, curr_sum)            
            curr_sum = min(0, curr_sum)
            
        return min_sum
