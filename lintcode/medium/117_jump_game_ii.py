'''
Link: https://www.lintcode.com/problem/117
'''

# My own solution. Should be correct, but hits time limit exceeded exception.
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        n = len(A)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(n):
            if dp[i] == float('inf'):
                break
            max_jump_len = A[i]
            for j in range(i + 1, i + max_jump_len + 1):
                if j >= n:
                    break
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[n - 1]



  
