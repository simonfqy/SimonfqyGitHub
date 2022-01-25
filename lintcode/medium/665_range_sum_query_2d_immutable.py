'''
Link: https://www.lintcode.com/problem/665
'''


# My own solution. Initially I used a (top_row, row, col) triplet as the key of dictionary, which caused a memory limit exceeded exception.
# This version only uses (row, col) to locate the value in the matrix. 
class NumMatrix:
    """
    @param: matrix: a 2D matrix
    """
    def __init__(self, matrix):
        self.coord_to_prefix_sum = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        prefix_sum_col = [0] * len(matrix[0])
        for row in range(len(matrix)):
            prefix_sum = 0
            for col in range(len(matrix[0])):
                prefix_sum_col[col] += matrix[row][col]
                prefix_sum += prefix_sum_col[col]
                self.coord_to_prefix_sum[row][col] = prefix_sum

    """
    @param: row1: An integer
    @param: col1: An integer
    @param: row2: An integer
    @param: col2: An integer
    @return: An integer
    """
    def sumRegion(self, row1, col1, row2, col2):
        bottom_right_sum = self.coord_to_prefix_sum[row2][col2]
        bottom_left_sum = 0
        if row1 > 0:
            bottom_right_sum -= self.coord_to_prefix_sum[row1 - 1][col2]
        if col1 > 0:
            bottom_left_sum = self.coord_to_prefix_sum[row2][col1 - 1]
            if row1 > 0:
                bottom_left_sum -= self.coord_to_prefix_sum[row1 - 1][col1 - 1]                     

        return bottom_right_sum - bottom_left_sum
      
      
