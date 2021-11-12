'''
Link: https://www.lintcode.com/problem/621
'''

# My own solution, uses heapq and two pointers. Has O(nlogn) time complexity due to heap operations.
import heapq
class Solution:
    """
    @param nums: an array of integers
    @param k1: An integer
    @param k2: An integer
    @return: the largest sum
    """
    def maxSubarray5(self, nums, k1, k2):
        if not nums or len(nums) < k1 or k2 < k1:
            return 0
        n = len(nums)
        max_subarray_sum = float('-inf')
        prefix_sum = 0
        prefix_sum_list = [0]
        for num in nums:
            prefix_sum += num
            prefix_sum_list.append(prefix_sum)
        prefix_sum_to_ind_heap = []
        for right in range(k1, n + 1):
            rightmost_ind_for_k1_window = right - k1
            heapq.heappush(prefix_sum_to_ind_heap, (prefix_sum_list[rightmost_ind_for_k1_window], rightmost_ind_for_k1_window))
            leftmost_ind_for_k2_window = right - k2   
            while True:
                min_prefix_sum, corresponding_ind = prefix_sum_to_ind_heap[0]
                if corresponding_ind >= leftmost_ind_for_k2_window:
                    break
                heapq.heappop(prefix_sum_to_ind_heap)
            subarray_sum = prefix_sum_list[right] - min_prefix_sum
            max_subarray_sum = max(max_subarray_sum, subarray_sum)            

        return max_subarray_sum
