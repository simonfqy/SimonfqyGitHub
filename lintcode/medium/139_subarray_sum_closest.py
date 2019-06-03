'''
Link: https://www.lintcode.com/problem/subarray-sum-closest/description
'''

# My own solution. Uses prefix sum array and custom-implemented Quicksort. Satisfies the O(nlogn) TC requirement.
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        prefix_sum = 0
        prefix_sum_and_ind_list = []
        for i, number in enumerate(nums):
            prefix_sum += number
            prefix_sum_and_ind_list.append((prefix_sum, i))
        self.sort_list(prefix_sum_and_ind_list, 0, len(prefix_sum_and_ind_list) - 1)
        prev_sum, prev_ind = 0, -1
        min_diff = None
        best_indices = [None, None]
        for prefix_sum, ind in prefix_sum_and_ind_list:
            diff = abs(prefix_sum - prev_sum)
            return_immediately = False
            if diff == 0:
                return_immediately = True
            if diff == 0 or min_diff is None or min_diff > diff:
                min_diff = diff
                best_indices = [min(prev_ind, ind) + 1, max(prev_ind, ind)]
            if return_immediately:
                return best_indices
            prev_sum, prev_ind = prefix_sum, ind
        return best_indices
        
        
    def sort_list(self, prefix_sum_and_ind_list, start, end):
        left, right = start, end
        if left >= right:
            return
        pivot, pivot_pos = prefix_sum_and_ind_list[(left + right) // 2]
        while left <= right:
            while left <= right and prefix_sum_and_ind_list[left][0] < pivot:
                left += 1
            while left <= right and prefix_sum_and_ind_list[right][0] > pivot:
                right -= 1
            if left <= right:
                prefix_sum_and_ind_list[left], prefix_sum_and_ind_list[right] = prefix_sum_and_ind_list[right], \
                    prefix_sum_and_ind_list[left]
                left += 1
                right -= 1
        self.sort_list(prefix_sum_and_ind_list, start, right)
        self.sort_list(prefix_sum_and_ind_list, left, end)
