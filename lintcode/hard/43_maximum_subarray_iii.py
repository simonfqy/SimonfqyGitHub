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

                
# A further improved version of the one above. Now we use more memoization. The time complexity has now been reduced to O(kn ^ 2).
# However, it still hits time limit exceeded exception, now much later throughout the test cases.
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        if not nums or k < 0 or len(nums) < k:
            return 0
        self.subarray_count_to_indices_to_max_sum = dict()
        self.populate_subarray_max_sum_dict(nums, k)
        return self.get_max_subarray_sum(nums, k)
    
    def populate_subarray_max_sum_dict(self, nums, k):
        n = len(nums)
        if 1 not in self.subarray_count_to_indices_to_max_sum:
            self.subarray_count_to_indices_to_max_sum[1] = dict()
        for start in range(n):
            prefix_sum = 0
            min_sum = 0
            max_sum_so_far = float('-inf')
            for end in range(start, n):
                prefix_sum += nums[end]
                max_sum_so_far = max(max_sum_so_far, prefix_sum - min_sum)
                self.subarray_count_to_indices_to_max_sum[1][(start, end)] = max_sum_so_far
                min_sum = min(min_sum, prefix_sum)
        
        for subarray_count in range(2, k):
            if subarray_count not in self.subarray_count_to_indices_to_max_sum:
                self.subarray_count_to_indices_to_max_sum[subarray_count] = dict()
            for composite_subarray_end_ind in range(subarray_count - 1, n - 1):
                max_composite_array_sum = float('-inf')
                for first_subarray_end_ind in range(subarray_count - 2, composite_subarray_end_ind):
                    left_max = self.subarray_count_to_indices_to_max_sum[subarray_count - 1][(0, first_subarray_end_ind)]
                    right_max = self.subarray_count_to_indices_to_max_sum[1][(first_subarray_end_ind + 1, composite_subarray_end_ind)]
                    max_composite_array_sum = max(max_composite_array_sum, left_max + right_max)
                self.subarray_count_to_indices_to_max_sum[subarray_count][(0, composite_subarray_end_ind)] = max_composite_array_sum

    def get_max_subarray_sum(self, nums, k):
        n = len(nums)
        if k == 1:
            return self.subarray_count_to_indices_to_max_sum[1][(0, n - 1)]
        prev_subarray_count = k - 1
        max_sum_so_far = float('-inf')
        for composite_subarray_end_ind in range(prev_subarray_count - 1, n - 1):
            left_max = self.subarray_count_to_indices_to_max_sum[prev_subarray_count][(0, composite_subarray_end_ind)]
            right_max = self.subarray_count_to_indices_to_max_sum[1][(composite_subarray_end_ind + 1, n - 1)]
            max_sum_so_far = max(max_sum_so_far, left_max + right_max)
        return max_sum_so_far
    

# A further improved version. Finally it passes. The time complexity should still be around O(kn ^ 2), but in fact it is much 
# improved compared to the one above.
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        if not nums or k < 0 or len(nums) < k:
            return 0
        self.subarray_count_to_indices_to_max_sum = dict()
        self.populate_subarray_max_sum_dict(nums, k)
        return self.get_max_subarray_sum(nums, k)
    
    def populate_subarray_max_sum_dict(self, nums, k):
        n = len(nums)
        self.subarray_count_to_indices_to_max_sum[1] = dict()
            
        for start in range(n):
            if k <= 1 and start > 0:
                break
            prefix_sum = 0
            min_sum = 0
            max_sum_so_far = float('-inf')
            for end in range(start, n): 
                prefix_sum += nums[end]
                max_sum_so_far = max(max_sum_so_far, prefix_sum - min_sum)
                min_sum = min(min_sum, prefix_sum)                
                self.subarray_count_to_indices_to_max_sum[1][(start, end)] = max_sum_so_far   
        
        for subarray_count in range(2, k):
            if subarray_count not in self.subarray_count_to_indices_to_max_sum:
                self.subarray_count_to_indices_to_max_sum[subarray_count] = dict()
            left_subarray_end_ind_yielding_max_total_sum = subarray_count - 2
            for composite_subarray_end_ind in range(subarray_count - 1, n - 1):
                if (0, composite_subarray_end_ind) in self.subarray_count_to_indices_to_max_sum[subarray_count]:
                    continue
                max_composite_array_sum = float('-inf')
                # This is the main optimization. The left_subarray_end_ind_yielding_max_total_sum is monotonically increasing for a given subarray_count.
                # This is because the nums[:left_subarray_end_ind_yielding_max_total_sum + 1] will host multiple subarrays, while the right hand side only
                # contains 1 subarray. The sums of subarrays will monotonically increase with the number of subarrays, even if they're operating on the same
                # nums list. That's because a finer granularity will keep the negative entries out, increasing the total sum. Hence, we should monotonically
                # increase left_subarray_end_ind_yielding_max_total_sum whenever a larger sum is found, and only start the next rounds of search from this
                # index, rather than starting from subarray_count - 2 all over again.
                starting_point_for_left_end_ind = max(subarray_count - 2, left_subarray_end_ind_yielding_max_total_sum)
                for first_subarray_end_ind in range(starting_point_for_left_end_ind, composite_subarray_end_ind):
                    left_max = self.subarray_count_to_indices_to_max_sum[subarray_count - 1][(0, first_subarray_end_ind)]
                    right_max = self.subarray_count_to_indices_to_max_sum[1][(first_subarray_end_ind + 1, composite_subarray_end_ind)]
                    if left_max + right_max > max_composite_array_sum:
                        max_composite_array_sum = left_max + right_max
                        left_subarray_end_ind_yielding_max_total_sum = max(left_subarray_end_ind_yielding_max_total_sum, first_subarray_end_ind)
                self.subarray_count_to_indices_to_max_sum[subarray_count][(0, composite_subarray_end_ind)] = max_composite_array_sum

    def get_max_subarray_sum(self, nums, k):
        n = len(nums)
        if k == 1:
            return self.subarray_count_to_indices_to_max_sum[1][(0, n - 1)]
        prev_subarray_count = k - 1
        max_sum_so_far = float('-inf')
        for composite_subarray_end_ind in range(prev_subarray_count - 1, n - 1):
            left_max = self.subarray_count_to_indices_to_max_sum[prev_subarray_count][(0, composite_subarray_end_ind)]
            right_max = self.subarray_count_to_indices_to_max_sum[1][(composite_subarray_end_ind + 1, n - 1)]
            max_sum_so_far = max(max_sum_so_far, left_max + right_max)
        return max_sum_so_far

