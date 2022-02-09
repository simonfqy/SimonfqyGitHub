'''
Link: https://www.lintcode.com/problem/76/
'''


# Solution from jiuzhang.com. DP, has O(n^2) time complexity.
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                dp[i] = max(dp[i], dp[j] + 1)
                
        return max(dp)
        
