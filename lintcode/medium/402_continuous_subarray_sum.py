'''
Link: https://www.lintcode.com/problem/402
'''

# My own solution. Uses prefix sum (single variable). Has O(n) time complexity and O(1) space complexity.
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
        # This variable actually makes this algorithm harder to maintain than the solution from jiuzhang.com, shown below.
        candidate_start_ind = 0
        for i, num in enumerate(A):
            prefix_sum += num
            # The maximum subarray sum among all subarrays ending at A[i].
            curr_max_subarray_sum = prefix_sum - min_sum
            if curr_max_subarray_sum > max_subarray_sum:
                max_subarray_sum = curr_max_subarray_sum
                end_ind = i
                start_ind = candidate_start_ind
            if prefix_sum < min_sum:
                min_sum = prefix_sum
                # Updated whenever prefix_sum is smaller than the smallest record. The candidate starting index is right after the 
                # index yielding the minimum prefix sum so far.
                candidate_start_ind = i + 1
        return [start_ind, end_ind]
    

# Solution from jiuzhang.com. Does not use prefix sum. Has O(n) time complexity and O(1) space complexity.
# Greedily maintains the starting and ending indices of the global max subarray, and the largest subarray ending at A[i]
# where i is the index when we traverse through A. It is less error prone than my own solution shown above. 
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        if not A:
            return [0, 0]
        # Starting and ending indices of the global max subarray.
        start, end = 0, 0
        # Starting index of the largest subarray ending at A[i] as we traverse through the array A.
        start_ind_of_curr_subarray = 0
        max_sum = float('-inf') 
        curr_max_subarray_sum = 0               
        for i, num in enumerate(A):
            if curr_max_subarray_sum < 0:
                start_ind_of_curr_subarray = i
                curr_max_subarray_sum = num
            else:
                curr_max_subarray_sum += num
            if curr_max_subarray_sum > max_sum:
                max_sum = curr_max_subarray_sum
                start = start_ind_of_curr_subarray
                end = i                        
        return [start, end]
    
