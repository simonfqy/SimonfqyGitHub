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
        
