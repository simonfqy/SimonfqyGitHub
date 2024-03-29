'''
Link: https://www.lintcode.com/problem/114/
'''

# My own solution, using memoized search. Has O(mn) time complexity.
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        self.m, self.n = m, n
        self.path_counts = [[None] * n for _ in range(m)]
        return self.get_path_count(0, 0)

    def get_path_count(self, row, col):
        if row >= self.m or col >= self.n:
            return 0
        if self.path_counts[row][col] is not None:
            return self.path_counts[row][col]
        if row == self.m - 1 and col == self.n - 1:
            return 1
        down_count = self.get_path_count(row + 1, col)
        right_count = self.get_path_count(row, col + 1)
        self.path_counts[row][col] = down_count + right_count
        return self.path_counts[row][col]
    
        
# My own solution using dp. Time complexity is also O(mn).
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        dp = [[0] * n for _ in range(m)]        
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row == m - 1: 
                    if col == n - 1:
                        dp[row][col] = 1
                        continue
                    dp[row][col] = dp[row][col + 1]
                    continue
                # Now row < m - 1
                dp[row][col] = dp[row + 1][col]
                if col < n - 1:
                    dp[row][col] += dp[row][col + 1]
        return dp[0][0]
    
    
# DP Solution from jiuzhang.com. Time complexity is O(mn). Logic is simpler than mine.
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]     
    
    
# Optimized DP Solution from jiuzhang.com, which replaces the 2D matrix in the above solution with 1d array. Time complexity is O(mn).
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        dp = [0] * n 
        dp[0] = 1
        for i in range(m):
            # Note that here j starts from 1, not 0.
            for j in range(1, n):                
                dp[j] += dp[j - 1]
        return dp[n - 1]       
    
    
# Solution from jiuzhang.com, which is a mathematics solution. Time complexity is O(min(m, n)).
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        if m >= n:
            m, n = n, m
        numerator = denominator = 1
        for i in range(1, m):
            denominator *= i
        for j in range(n, m + n - 1):
            numerator *= j
        return numerator // denominator  
    
    
