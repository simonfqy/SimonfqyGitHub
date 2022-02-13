'''
Link: https://www.lintcode.com/problem/1645
'''


# Solution from jiuzhang.com. Uses dynamic programming. Has O(n^2) time complexity.
class Solution:
    """
    @param arrayIn: The original array.
    @return: Count the minimum number of subarrays.
    """
    def LeastSubsequences(self, arrayIn):
        n = len(arrayIn)
        if n <= 1:
            return n
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if arrayIn[j] > arrayIn[i]:
                    continue
                dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

                
