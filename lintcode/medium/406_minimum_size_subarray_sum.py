'''
Link: https://www.lintcode.com/problem/406
'''

# My own solution. Using two pointers, time complexity is O(n).
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        min_length = float('inf')
        end_ind, sum_so_far = 0, 0
        for start_ind in range(len(nums)):
            end_ind = max(start_ind, end_ind)
            curr_length = float('inf')
            while end_ind < len(nums) and sum_so_far + nums[end_ind] < s:
                sum_so_far += nums[end_ind]
                end_ind += 1
            if end_ind < len(nums) and sum_so_far + nums[end_ind] >= s:
                curr_length = end_ind + 1 - start_ind
            # Both conditions below are okay: we don't need to include the sum_so_far < s condition. But it can
            # still be added for extra clarity.
            # elif end_ind == len(nums) and sum_so_far < s:
            elif end_ind == len(nums):
                break
            if curr_length == 1:
                return 1
            if curr_length < min_length:
                min_length = curr_length
            sum_so_far -= nums[start_ind]
        if min_length < float('inf'):
            return min_length
        return -1          
    
    
# My own solution. Uses a prefix sum list and two pointers to solve the problem, time complexity is also O(n).
# The performance is slightly better than the solution above, but the code is more complicated.
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        prefix_sum_list = []
        sum_so_far = 0
        n = len(nums)
        for num in nums:
            sum_so_far += num
            prefix_sum_list.append(sum_so_far)
        if not prefix_sum_list or prefix_sum_list[-1] < s:
            return -1
        start_ind = 0
        min_length = float('inf')
        # i is the ending index (inclusive).
        for i in range(n):
            if prefix_sum_list[i] < s:
                continue        
            curr_length = float('inf')    
            # A Pythonic do-while loop.
            while True:
                if start_ind > 0:
                    subarray_sum = prefix_sum_list[i] - prefix_sum_list[start_ind - 1]
                else:
                    subarray_sum = prefix_sum_list[i]
                if subarray_sum >= s:
                    curr_length = i - start_ind + 1
                if start_ind >= i or subarray_sum < s:
                    break
                start_ind += 1            
            if curr_length == 1:
                return 1
            if curr_length < min_length:
                min_length = curr_length
        if min_length < float('inf'):
            return min_length
        return -1
    

# This solution is from jiuzhang.com, I only slightly modified it. It is simpler than my first solution. 
import sys
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        min_length = sys.maxsize
        n = len(nums)
        sum_so_far = 0
        end_ind = 0
        for start_ind in range(n):
            # Here we don't assign the end_ind to be the max of (end_ind, start_ind); and we directly use sum_so_far in the condition
            # of the while loop, not sum_so_far + nums[end_ind]. This simplifies the logic.
            while end_ind < n and sum_so_far < s:
                sum_so_far += nums[end_ind]
                end_ind += 1
            if sum_so_far >= s:
                min_length = min(min_length, end_ind - start_ind)
            else:
                # end_ind == n, but sum is smaller than s. So there's no point continuing.
                break
            if min_length == 1:
                break
            sum_so_far -= nums[start_ind]

        return -1 if min_length == sys.maxsize else min_length
