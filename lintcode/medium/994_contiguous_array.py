'''
Link: https://www.lintcode.com/problem/994
'''

# My own solution. Should be correct, but hits time limit exceeded exception. Has O(n^2) time complexity.
class Solution:
    """
    @param nums: a binary array
    @return: the maximum length of a contiguous subarray
    """
    def findMaxLength(self, nums):
        if not nums:
            return 0
        max_length = 0
        n = len(nums)
        one_count, zero_count = 0, 0
        for right in range(n):
            one_count += nums[right] == 1
            zero_count += nums[right] == 0
            running_one_count = one_count
            running_zero_count = zero_count
            for left in range(right):
                length = right + 1 - left
                if length - max_length <= abs(running_one_count - running_zero_count):
                    break
                if length % 2 == 0 and running_one_count == running_zero_count:
                    max_length = length
                    break
                running_one_count -= nums[left] == 1
                running_zero_count -= nums[left] == 0
        return max_length
    
                
# My own solution, passes the tests with good performance. Has O(n) time complexity. Converts 0s to -1s, and transforms this problem into the
# subarray sum zero problem. Can be accomplished by dictionary (hashmap), with a single traversal of the array.
class Solution:
    """
    @param nums: a binary array
    @return: the maximum length of a contiguous subarray
    """
    def findMaxLength(self, nums):
        n = len(nums)
        prefix_sum = 0
        prefix_sum_to_ind = {0: -1}
        max_length = 0
        for i, num in enumerate(nums):
            if num == 1:
                prefix_sum += 1
            else:
                prefix_sum -= 1
            if prefix_sum not in prefix_sum_to_ind:                
                prefix_sum_to_ind[prefix_sum] = i
            else:
                length = i - prefix_sum_to_ind[prefix_sum]
                max_length = max(max_length, length)        
        return max_length
