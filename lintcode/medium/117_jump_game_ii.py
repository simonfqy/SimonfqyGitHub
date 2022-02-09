'''
Link: https://www.lintcode.com/problem/117
'''

# My own solution. Has O(n) time complexity. Uses greedy algorithm and dynamic programming.
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        n = len(A)
        dp = [float('inf')] * n
        dp[0] = 0
        # If we don't use this frontier variable to eliminate some futile searches, it will hit time limit exceeded exception.
        frontier = 0
        for i in range(n):
            if i > frontier:
                break
            max_jump_len = A[i]
            for j in range(frontier + 1, i + max_jump_len + 1):
                if j >= n:
                    break
                dp[j] = min(dp[j], dp[i] + 1)
            frontier = max(frontier, i + max_jump_len)
        return dp[n - 1]

  
