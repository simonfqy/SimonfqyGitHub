'''
Link: https://www.lintcode.com/problem/911
'''

# My own solution. Should be correct, but hits time limit exceeded exception. Time complexity is O(n^2).
class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        if not nums:
            return 0
        longest = 0
        # subarray_sum, left = 0, 0
        n = len(nums)        
        prefix_sum = 0
        prefix_sum_list = [0]
        for num in nums:
            prefix_sum += num
            prefix_sum_list.append(prefix_sum)
        # starting_ind_to_sum = defaultdict(int)
        for right in range(1, n + 1):
            prefix_sum = prefix_sum_list[right]            
            for left in range(right):
                subarray_sum = prefix_sum - prefix_sum_list[left]
                if subarray_sum == k:
                    longest = max(longest, right - left)
                    break

        return longest
