'''
Link: https://www.lintcode.com/problem/window-sum/description
'''

# My own solution.
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        n = len(nums)
        if n <= 0:
            return []
        if n <= k:
            return [sum(nums)]
        res = []
        sum_val = sum(nums[:k])
        res.append(sum_val)
        for i in range(n - k):
            sum_val = sum_val - nums[i] + nums[i + k]
            res.append(sum_val)
        return res
