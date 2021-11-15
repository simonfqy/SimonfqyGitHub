'''
https://www.lintcode.com/problem/620
'''

# My own solution. Uses 2 pointer, but still has O(n^2) time complexity.
class Solution:
    """
    @param nums: an array of integer
    @param k: an integer
    @return: the largest sum
    """
    def maxSubarray4(self, nums, k):
        if not nums or len(nums) < k:
            return 0
        n = len(nums)
        prefix_sum = 0
        prefix_sum_list = [0]
        for num in nums:
            prefix_sum += num
            prefix_sum_list.append(prefix_sum)
        min_sum = float('inf')
        max_subarray_sum = prefix_sum_list[k]
        start = 1
        while start < n - k + 2:
            if prefix_sum_list[start - 1] >= min_sum:
                start += 1
                continue
            min_sum = prefix_sum_list[start - 1]
            end = start + k - 1
            while end < n + 1:
                latest_possible_start_ind = end - k + 1                
                min_sum = min(min_sum, prefix_sum_list[latest_possible_start_ind - 1])
                max_subarray_sum = max(max_subarray_sum, prefix_sum_list[end] - min_sum)
                end += 1
            start += 1

        return max_subarray_sum
    
    
# My own solution. Uses 1 pointer (sliding window), has O(n) time complexity.
class Solution:
    """
    @param nums: an array of integer
    @param k: an integer
    @return: the largest sum
    """
    def maxSubarray4(self, nums, k):
        if not nums or len(nums) < k:
            return 0
        n = len(nums)
        prefix_sum = 0
        prefix_sum_list = [0]
        for num in nums:
            prefix_sum += num
            prefix_sum_list.append(prefix_sum)
        min_sum = float('inf')
        max_subarray_sum = float('-inf')        
        for right in range(k, n + 1):
            min_sum = min(min_sum, prefix_sum_list[right - k])
            max_subarray_sum = max(max_subarray_sum, prefix_sum_list[right] - min_sum)

        return max_subarray_sum
    
    # This is an alternative implementation, in which min_sum was initialized to 0 and was assigned value after max_subarray_sum in each iteration of the for loop.
    # It is equivalent to the implementation above.
    def maxSubarray4_alternative(self, nums, k):
        if not nums or len(nums) < k:
            return 0
        n = len(nums)
        prefix_sum = 0
        prefix_sum_list = [0]
        for num in nums:
            prefix_sum += num
            prefix_sum_list.append(prefix_sum)
        min_sum = 0
        max_subarray_sum = float('-inf')        
        for right in range(k, n + 1):            
            max_subarray_sum = max(max_subarray_sum, prefix_sum_list[right] - min_sum)
            min_sum = min(min_sum, prefix_sum_list[right - k + 1])

        return max_subarray_sum
    
    
# Solution from jiuzhang.com. Compared to my solution above, it is more optimized in that the space complexity is reduced from O(n) to O(1),
# because we no longer need to maintain a prefix sum array, just two variables to record the running prefix sum of the left and right pointers
# as we traverse the array. 
class Solution:
    """
    @param nums: an array of integer
    @param k: an integer
    @return: the largest sum
    """
    def maxSubarray4(self, nums, k):
        if not nums or len(nums) < k:
            return 0
        n = len(nums)        
        min_sum = 0             
        right_sum, left_sum = 0, 0
        for i in range(k):
            right_sum += nums[i]
        max_subarray_sum = right_sum 
        for right in range(k, n):
            left_sum += nums[right - k]
            right_sum += nums[right]
            min_sum = min(min_sum, left_sum)
            max_subarray_sum = max(max_subarray_sum, right_sum - min_sum)

        return max_subarray_sum
