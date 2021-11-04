'''
Link: https://www.lintcode.com/problem/43
'''

# My own solution. Should be correct, but hits time limit exceeded exception. The time complexity is O(n^(min(1, k - 1))).
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        if not nums or len(nums) < k:
            return 0
        
        n = len(nums)
        left_summer_count = k - 1
        right_summer_count = 1
        if k == 1:
            left_summer_count = 1
            right_summer_count = 0
        right_max_sums = None
        if right_summer_count > 0:
            right_sum = 0
            right_max_sums = [0] * n
            curr_largest_subarray_sum = 0
            max_sum_so_far = float('-inf')
            for j in range(n - 1, left_summer_count - 1, -1):
                curr_largest_subarray_sum = max(curr_largest_subarray_sum + nums[j], nums[j])
                max_sum_so_far = max(max_sum_so_far, curr_largest_subarray_sum)
                right_max_sums[j] = max_sum_so_far         
        
        return self.get_max_total_sum(nums, 0, left_summer_count, right_max_sums)

    def get_max_total_sum(self, nums, start, remaining_left_summer_count, right_max_sums):
        if remaining_left_summer_count == 1:
            end = len(nums) - 1
            if not right_max_sums:
                right_max_sums = [0] * (len(nums) + 1)
                end = len(nums)

            max_sum_so_far = float('-inf')
            curr_largest_subarray_sum = 0
            max_subarray_sum_on_left = list(nums)
            for i in range(start, len(nums)):
                curr_largest_subarray_sum = max(curr_largest_subarray_sum + nums[i], nums[i])
                max_sum_so_far = max(max_sum_so_far, curr_largest_subarray_sum)
                max_subarray_sum_on_left[i] = max_sum_so_far
            max_total_sum = float('-inf')
        
            for i in range(start, end):
                max_total_sum = max(max_total_sum, max_subarray_sum_on_left[i] + right_max_sums[i + 1])
            return max_total_sum
        
        max_total_sum, left_max_sum = float('-inf'), float('-inf')
        curr_largest_subarray_sum = 0
        for i in range(start, len(nums) - remaining_left_summer_count):
            curr_largest_subarray_sum = max(curr_largest_subarray_sum + nums[i], nums[i])
            left_max_sum = max(left_max_sum, curr_largest_subarray_sum)
            right_side_max_sum = self.get_max_total_sum(nums, i + 1, remaining_left_summer_count - 1, right_max_sums)
            max_total_sum = max(max_total_sum, left_max_sum + right_side_max_sum)
        return max_total_sum
    

# My own solution, improves upon the previous solution by using memoization. Should be correct, but still hits time limit exceeded exception. 
# The time complexity is O(n ^ min(1, k - 1)).
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        if not nums or len(nums) < k:
            return 0
        self.start_end_inds_to_max_single_subarray_sum = dict()
        n = len(nums)
        left_summer_count = max(1, k - 1)
        right_summer_count = min(k - 1, 1)
        self.find_all_max_single_subarray_sums(nums)
                
        return self.get_max_total_sum(nums, 0, left_summer_count, right_summer_count)

    def get_max_total_sum(self, nums, start, remaining_left_summer_count, right_summer_count):
        if remaining_left_summer_count == 1:
            max_total_sum = float('-inf')
            if right_summer_count > 0:
                for i in range(start, len(nums) - 1):
                    left_side_max = self.start_end_inds_to_max_single_subarray_sum[(start, i)]
                    right_side_max = self.start_end_inds_to_max_single_subarray_sum[(i + 1, len(nums) - 1)]
                    max_total_sum = max(max_total_sum, left_side_max + right_side_max)
            else:
                for i in range(start, len(nums)):     
                    max_total_sum = max(max_total_sum, self.start_end_inds_to_max_single_subarray_sum[(start, i)])

            return max_total_sum
        
        max_total_sum = float('-inf')
        for i in range(start, len(nums) - remaining_left_summer_count):
            left_max_sum = self.start_end_inds_to_max_single_subarray_sum[(start, i)]
            right_max_sum = self.get_max_total_sum(nums, i + 1, remaining_left_summer_count - 1, right_summer_count)
            max_total_sum = max(max_total_sum, left_max_sum + right_max_sum)
        return max_total_sum

    def find_all_max_single_subarray_sums(self, nums):
        n = len(nums)
        for start in range(n):
            curr_largest_subarray_sum = 0
            max_sum_so_far = float('-inf')
            for end in range(start, n):
                curr_largest_subarray_sum = max(curr_largest_subarray_sum + nums[end], nums[end])
                max_sum_so_far = max(max_sum_so_far, curr_largest_subarray_sum)
                self.start_end_inds_to_max_single_subarray_sum[(start, end)] = max_sum_so_far

