'''
https://www.lintcode.com/problem/45
'''


# My implementation based on the instruction from jiuzhang.com. Uses Dynamic Programming, takes O(n) time and space complexity.
# I initially did not think of using prefix sum to calculate the maximum and minimum subarrays, which turned out to be too complicated.
# Having the right mental model can simplify things a LOT.
class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    def maxDiffSubArrays(self, nums):     
        if not nums or len(nums) <= 1:
            return 0   
        max_diff = 0
        n = len(nums)
        # Left side is inclusive, right side is not.
        left_side_max_subarray_sum, left_side_min_subarray_sum = dict(), dict()
        right_side_max_subarray_sum, right_side_min_subarray_sum = dict(), dict()
        prefix_sum = 0
        min_sum, max_sum = 0, 0
        left_max, left_min = float('-inf'), float('inf')
        for i in range(n - 1):
            prefix_sum += nums[i]
            left_max = max(left_max, prefix_sum - min_sum)
            left_min = min(left_min, prefix_sum - max_sum)
            left_side_max_subarray_sum[i] = left_max
            left_side_min_subarray_sum[i] = left_min
            min_sum = min(min_sum, prefix_sum)
            max_sum = max(max_sum, prefix_sum)

        right_hand_sum = 0
        min_sum, max_sum = 0, 0
        right_max, right_min = float('-inf'), float('inf')
        for j in range(n - 2, -1, -1):
            right_hand_sum += nums[j + 1]
            right_max = max(right_max, right_hand_sum - min_sum)
            right_min = min(right_min, right_hand_sum - max_sum)
            right_side_max_subarray_sum[j] = right_max
            right_side_min_subarray_sum[j] = right_min
            min_sum = min(min_sum, right_hand_sum)
            max_sum = max(max_sum, right_hand_sum)
         
        for i in range(n - 1):
            max_diff = max(max_diff, left_side_max_subarray_sum[i] - right_side_min_subarray_sum[i], \
                    right_side_max_subarray_sum[i] - left_side_min_subarray_sum[i])
        return max_diff
    
    
# Solution from jiuzhang.com. Uses dynamic programming and greedy algorithm. Very similar to the solution above, but simpler because
# we use greedy algorithm to determine the maximum sum subarray ending at index i when we're traversing the nums array.
class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    def maxDiffSubArrays(self, nums):
        n = len(nums)
        min_sum_on_left, min_sum_on_right = [0] * n, [0] * n
        max_sum_on_left, max_sum_on_right = [0] * n, [0] * n
        min_sum_on_left[0] = max_sum_on_left[0] = nums[0]
        max_sum_on_right[n - 1] = min_sum_on_right[n - 1] = nums[n - 1]
        current_subarray_sum_min = current_subarray_sum_max = nums[0]
        for i in range(1, n):
            # Greedy algorithm: current_subarray_sum_max is the sum of the maximum sum subarray ending at index i. If the current_subarray_sum_max
            # is not the largest sum subarray in nums[:i + 1], then it should be equal to max_sum_on_left[i - 1], which is a subarray ending at 
            # index i - 1 or earlier.
            current_subarray_sum_max = max(current_subarray_sum_max + nums[i], nums[i])
            current_subarray_sum_min = min(current_subarray_sum_min + nums[i], nums[i])
            max_sum_on_left[i] = max(max_sum_on_left[i - 1], current_subarray_sum_max)
            min_sum_on_left[i] = min(min_sum_on_left[i - 1], current_subarray_sum_min)
        current_subarray_sum_min = current_subarray_sum_max = nums[n - 1]
        for j in range(n - 2, -1, -1):
            current_subarray_sum_max = max(current_subarray_sum_max + nums[j], nums[j])
            current_subarray_sum_min = min(current_subarray_sum_min + nums[j], nums[j])
            max_sum_on_right[j] = max(max_sum_on_right[j + 1], current_subarray_sum_max)
            min_sum_on_right[j] = min(min_sum_on_right[j + 1], current_subarray_sum_min)
        max_diff = 0
        for i in range(n - 1):
            max_diff = max(max_diff, max_sum_on_left[i] - min_sum_on_right[i + 1], max_sum_on_right[i + 1] - min_sum_on_left[i])
        return max_diff
        
