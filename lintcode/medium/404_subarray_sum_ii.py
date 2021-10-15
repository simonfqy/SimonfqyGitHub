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
    
    
# An optimized version of the previous solution, but still causes time limit exceeded exception.
class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        prefix_sum_list = []
        count = 0
        curr_sum = 0
        can_start_subarray_from_ind = [True] * len(A)
        for i, num in enumerate(A):
            curr_sum += num
            prefix_sum_list.append(curr_sum)

        for i in range(len(A)):
            if i == 0:
                prefix_sum = 0
            else:
                prefix_sum = prefix_sum_list[i - 1]
            subarray_sum = prefix_sum_list[-1] - prefix_sum
            if subarray_sum < start:
                for j in range(i, len(A)):
                    can_start_subarray_from_ind[j] = False
                break

        # Go through the list and check whether the subarray sum is too large. i should be the 
        # ending index.
        for i, prefix_sum in enumerate(prefix_sum_list):            
            # Start the subarray index from 0 to i. j is the starting index.
            for j in range(i, -1, -1):
                if not can_start_subarray_from_ind[j]:
                    break
                if j == 0:
                    prev_sum = 0
                else:
                    prev_sum = prefix_sum_list[j - 1]
                past_subarray_sum = prefix_sum - prev_sum
                if past_subarray_sum > end:
                    # From now on, we cannot start from j or any earlier elements. Otherwise the subarray sum will be too large.
                    for k in range(j, -1, -1):
                        can_start_subarray_from_ind[k] = False
                    continue
                if past_subarray_sum < start:
                    continue
                count += 1     
        return count              

                  
