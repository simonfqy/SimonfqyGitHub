'''
https://www.lintcode.com/problem/404
'''

# My own solution. Should be correct, but causes time limit exceeded exception.
class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        prefix_sum = []
        curr_sum = 0
        count = 0
        for i, num in enumerate(A):
            curr_sum += num
            prefix_sum.append(curr_sum)
            count += start <= curr_sum <= end
            for starting_ind in range(1, i + 1):
                subarray_sum = prefix_sum[i] - prefix_sum[starting_ind - 1]
                count += start <= subarray_sum <= end
        return count

