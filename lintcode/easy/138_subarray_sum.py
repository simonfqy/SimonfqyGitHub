'''
Link: https://www.lintcode.com/problem/subarray-sum/description
'''

# Uses prefix sum and dictionary.
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        if nums is None or len(nums) <= 0:
            return None 
        prefix_sum_to_ind = dict()
        curr_sum = 0
        for i, number in enumerate(nums):
            curr_sum += number
            if curr_sum == 0:
                return [0, i]
            if curr_sum in prefix_sum_to_ind:
                return [prefix_sum_to_ind[curr_sum] + 1, i]
            prefix_sum_to_ind[curr_sum] = i
