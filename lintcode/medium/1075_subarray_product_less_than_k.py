'''
Link: https://www.lintcode.com/problem/1075
'''

# My own solution. Using two pointers, has O(n) time complexity.
class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the number of subarrays where the product of all the elements in the subarray is less than k
    """
    def numSubarrayProductLessThanK(self, nums, k):
        if not nums or k <= 1:
            return 0
        n = len(nums)
        product = 1
        left = 0
        result = 0
        for right in range(n):
            product *= nums[right]
            while product >= k:
                product /= nums[left]
                left += 1
            if left > right:
                continue
            length = right - left + 1
            # At the current iteration, we only need to add those contiguous subarrays who end at nums[right]. They start at nums[left], 
            # nums[left + 1], ..., nums[right], so there are in total a {length} number of such subarrays.
            result += length
        return result
