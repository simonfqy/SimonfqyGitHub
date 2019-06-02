'''
Link: https://www.lintcode.com/problem/triangle/description
'''

# Correct, but causes time limit exceeded problem.
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        return self.minimum_triang(triangle, 0, 0)
        
    def minimum_triang(self, triangle, start_row, start_ind):
        if start_row >= len(triangle):
            return 0
        left_min = self.minimum_triang(triangle, start_row + 1, start_ind)
        right_min = self.minimum_triang(triangle, start_row + 1, start_ind + 1)
        return triangle[start_row][start_ind] + min(left_min, right_min)
