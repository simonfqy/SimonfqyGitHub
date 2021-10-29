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
                sum_to_col = dict()
                for col in range(n_col):
                    if row == 0:
                        base_sum = 0
                    else:
                        base_sum = submatrix_sum_matrix[row - 1][col]
                    corner_sum = submatrix_sum_matrix[running_row][col]
                    diff = corner_sum - base_sum
                    if diff == 0:
                        return [[row, 0], [running_row, col]]
                    if diff in sum_to_col:                        
                        return [[row, sum_to_col[diff] + 1], [running_row, col]]
                    sum_to_col[diff] = col
    
    
# Answer from jiuzhang.com. It is very similar to my solution above, but it is simpler: it avoids building a prefix sum matrix
# before actually finding the zero submatrix sum. Now the prefix sum is built on the go. There is some wasted work in calculating
# the sum for each column while traversing, but the time complexity is unchanged. 
# Using prefix sum. Let sums_for_each_column[j] = sum[0][j] + sum[1][j] + ... + sum[i][j]. It converts this problem into finding the subarray 
# sum zero in a row of the matrix.
class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """
    def submatrixSum(self, matrix):
        if not matrix or not matrix[0]:
            return None
        n, m = len(matrix), len(matrix[0])
        for top in range(n):
            sums_for_each_column = [0] * m
            for down in range(top, n):
                # It also adds {0: -1} to the dictionary early on, so we don't need to handle the case where prefix_sum == 0 separately.
                sum_to_col = {0: -1}
                prefix_sum = 0
                for col in range(m):
                    sums_for_each_column[col] += matrix[down][col]
                    # Now this problem is converted to a subarray sum zero problem and can be solved easily.
                    prefix_sum += sums_for_each_column[col]
                    if prefix_sum in sum_to_col:
                        return [[top, sum_to_col[prefix_sum] + 1], [down, col]]
                    sum_to_col[prefix_sum] = col

