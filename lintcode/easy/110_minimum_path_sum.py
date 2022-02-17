'''
Link: https://www.lintcode.com/problem/110/
'''


# My own solution. Dynamic programming, has O(mn) time complexity.
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]        
        for row in range(m):
            for col in range(n):
                dp[row][col] = grid[row][col]
                if row == 0 and col == 0:
                    continue
                if row == 0:
                    dp[row][col] += dp[row][col - 1]
                    continue
                if col == 0:
                    dp[row][col] += dp[row - 1][col]
                    continue
                dp[row][col] += min(dp[row][col - 1], dp[row - 1][col])
        return dp[m - 1][n - 1]

