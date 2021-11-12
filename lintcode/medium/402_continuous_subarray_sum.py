'''
Link: https://www.lintcode.com/problem/402
'''

# My own solution. Uses prefix sum array. Has O(n) time complexity and O(1) space complexity.
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        if not A:
            return [0, 0]
        max_subarray_sum = float('-inf')
        min_sum = 0
        prefix_sum = 0
        start_ind, end_ind = 0, 0
        candidate_start_ind = 0
        for i, num in enumerate(A):
            prefix_sum += num
            subarray_sum = prefix_sum - min_sum
            if subarray_sum > max_subarray_sum:
                max_subarray_sum = subarray_sum
                end_ind = i
                start_ind = candidate_start_ind
            if prefix_sum < min_sum:
                min_sum = prefix_sum
                candidate_start_ind = i + 1
        return [start_ind, end_ind]

