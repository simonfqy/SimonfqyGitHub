'''
https://www.lintcode.com/problem/617
'''

# My own solution, uses dynamic programming (in fact it is greedy algorithm, because we only need to keep 1 variable rather than an array, see the optimized 
# version below). Time complexity is O(n). Took an incredible amount of work to come up with.
class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        n = len(nums)
        prefix_sum = 0
        prefix_sum_list = [0]
        for num in nums:
            prefix_sum += num
            prefix_sum_list.append(prefix_sum)
        # The ind_right_before_local_max_avg[i] is the index right before the starting index of the maximum average subarray ending at prefix_sum_list[i].
        ind_right_before_local_max_avg = [0] * (n + 1)
        max_avg = float('-inf')
        for right in range(k, n + 1):
            ind_right_before_len_k_subarray = right - k
            prefix_sum_before_subarray = prefix_sum_list[ind_right_before_len_k_subarray]
            # The qualifying maximum average subarray ending at prefix_sum_list[right] can either be immediately after right - k (index in prefix_sum_list), or 
            # immediately after ind_right_before_local_max_avg[right - 1] (meaning we continue constructing the previously maximum average subarray), these 
            # are the only two possibilities. 
            curr_len_k_subarray_avg = (prefix_sum_list[right] - prefix_sum_before_subarray) / k
            ind_before_prev_local_max_start = ind_right_before_local_max_avg[right - 1]
            curr_longer_subarray_avg = (prefix_sum_list[right] - prefix_sum_list[ind_before_prev_local_max_start]) / (right - ind_before_prev_local_max_start)
            max_avg = max(max_avg, curr_len_k_subarray_avg, curr_longer_subarray_avg)
            if curr_len_k_subarray_avg > curr_longer_subarray_avg:
                ind_right_before_local_max_avg[right] = ind_right_before_len_k_subarray
            else:
                ind_right_before_local_max_avg[right] = ind_before_prev_local_max_start           

        return max_avg
      
      
# Optimized version of the solution above, using greedy algorithm. Time and space complexities are still both O(n). 
class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        n = len(nums)
        prefix_sum = 0
        prefix_sum_list = [0]
        for num in nums:
            prefix_sum += num
            prefix_sum_list.append(prefix_sum)
        ind_right_before_local_max_avg = 0
        max_avg = float('-inf')
        for right in range(k, n + 1):
            ind_right_before_len_k_subarray = right - k            
            curr_len_k_subarray_avg = (prefix_sum_list[right] - prefix_sum_list[ind_right_before_len_k_subarray]) / k
            ind_before_prev_local_max_start = ind_right_before_local_max_avg
            curr_longer_subarray_avg = (prefix_sum_list[right] - prefix_sum_list[ind_before_prev_local_max_start]) / (right - ind_before_prev_local_max_start)
            max_avg = max(max_avg, curr_len_k_subarray_avg, curr_longer_subarray_avg)
            if curr_len_k_subarray_avg > curr_longer_subarray_avg:
                ind_right_before_local_max_avg = ind_right_before_len_k_subarray                       

        return max_avg
    
    
# Solution from jiuzhang.com. Uses binary search on result. Has O(nlog(max-min)) time complexity. 
class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        start, end = min(nums), max(nums)
        while start + 1e-7 < end:
            mid = (start + end) / 2
            if self.candidate_avg_not_too_large(nums, k, mid):
                start = mid
            else:
                end = mid
        return start

    def candidate_avg_not_too_large(self, nums, k, candidate_avg):
        n = len(nums)
        prefix_sum_list = [0]
        prefix_sum = 0
        # Subtract each number by the candidate average value.
        for num in nums:
            prefix_sum += num - candidate_avg
            prefix_sum_list.append(prefix_sum)
        min_left_presum = 0
        for right in range(k, n + 1):
            min_left_presum = min(min_left_presum, prefix_sum_list[right - k])
            # If any subarray (with each element subtracted by the candidate average value) with length at least k has sum at least 0, it means
            # the largest subarray (length >= k) average is equal to or more than the candidate average. In this case we return True, and in 
            # the binary search, the candidate value is assigned to the start variable.
            if prefix_sum_list[right] - min_left_presum >= 0:
                return True
        return False
