'''
Link: https://www.lintcode.com/problem/403
'''

# My own solution which does not work correctly. I was trying to reuse my solution for question 402, but this case is different and this solution
# is incorrect.
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, A):
        if not A:
            return [0, 0]
        presum_list = [0]
        presum = 0
        n = len(A)
        for i in range(2 * n):
            presum += A[i % n]
            presum_list.append(presum)
        min_sum = 0
        start, end = 0, 0
        candidate_start = 0
        max_subarray_sum = float('-inf')
        for i in range(1, 2 * n + 1):
            curr_subarray_sum = presum_list[i] - min_sum
            if curr_subarray_sum > max_subarray_sum:
                max_subarray_sum = curr_subarray_sum
                end = (i - 1) % n
                start = candidate_start

            if i <= n and min_sum > presum_list[i]:
                min_sum = presum_list[i]
                candidate_start = i % n
             
        return [start, end]
