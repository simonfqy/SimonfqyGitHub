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

# A faster solution. The official one from Jiuzhang.com.    
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        n = len(nums)
        if n < k or k <= 0:
            return []
        res = [0] * (n - k + 1)
        res[0] = sum(nums[:k])
        for i in range(0, n - k):
            res[i + 1] = res[i] - nums[i] + nums[i + k]
            
        return res
