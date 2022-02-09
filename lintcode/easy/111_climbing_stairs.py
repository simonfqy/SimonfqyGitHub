'''
Link: https://www.lintcode.com/problem/111/
'''


# My own DP solution. Has O(n) time complexity.
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        if n < 1:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i] += dp[i - 1]
            if i > 1:
                dp[i] += dp[i - 2]
        return dp[n]
      
      
