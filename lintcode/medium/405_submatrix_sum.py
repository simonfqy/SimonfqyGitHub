'''
Link: https://www.lintcode.com/problem/405
'''

# My own solution. Should have O(n^3) time complexity, where n is the number of rows or columns.
# It creates a matrix containing the submatrix sum starting from (0, 0) coordinate, and finds the zero sum submatrix based on it.
class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """
    def submatrixSum(self, matrix):
        n_row = len(matrix)
        n_col = len(matrix[0])
        submatrix_sum_matrix = []
        for row in range(n_row):            
            new_row = []
            row_sum = 0
            for col in range(n_col):
                row_sum += matrix[row][col]
                if row == 0:
                    new_row.append(row_sum)
                else:
                    new_element = submatrix_sum_matrix[row - 1][col] + row_sum
                    new_row.append(new_element)                
            submatrix_sum_matrix.append(new_row)
        
        for row in range(n_row):
            # For each iteration, we consider the submatrix sum which starts from (row, 0)            
            for running_row in range(row, n_row):
                sum_to_coord = dict()
                for col in range(n_col):
                    if row == 0:
                        base_sum = 0
                    else:
                        base_sum = submatrix_sum_matrix[row - 1][col]
                    corner_sum = submatrix_sum_matrix[running_row][col]
                    diff = corner_sum - base_sum
                    if diff == 0:
                        return [[row, 0], [running_row, col]]
                    if diff in sum_to_coord:
                        _, y = sum_to_coord[diff]
                        return [[row, y + 1], [running_row, col]]
                    sum_to_coord[diff] = [running_row, col]
    
