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
            
            
# My own solution. It works, but the time to execute is really long.
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        for start in range(len(nums)):
            subarray_sum = 0
            for end in range(start, len(nums)):
                subarray_sum += nums[end]
                if subarray_sum == 0:
                    return [start, end]
                
                
# My own solution which uses prefix sum. Around the same performance as the one above.
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        prefix_sum = []
        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum == 0:
                return [0, i]
            prefix_sum.append(curr_sum)
        for start in range(1, len(nums)):
            for end in range(start, len(nums)):
                subarray_sum = prefix_sum[end] - prefix_sum[start - 1]
                if subarray_sum == 0:
                    return [start, end]                
                
                
# My own solution. It should work, but causes time limit exceeded exception.
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        n = len(nums)
        self.ind_to_sum = dict()
        for length in range(1, n + 1):
            for start in range(n):            
                end = start + length - 1
                if end >= n:
                    break
                if start == end:
                    self.ind_to_sum[(start, end)] = nums[start]
                else:
                    self.ind_to_sum[(start, end)] = self.ind_to_sum[(start, end - 1)] + nums[end]
                    del self.ind_to_sum[(start, end - 1)]
                if self.ind_to_sum[(start, end)] == 0:
                    return [start, end]
