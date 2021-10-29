'''
Link: https://www.lintcode.com/problem/944
'''

# My own solution. Has O(n^3) time complexity. Very similar to the solution used for problem 405:
# https://github.com/simonfqy/SimonfqyGitHub/blob/f0221a5adc6d132ac47becffe8a74a8b9f7e80ba/lintcode/medium/405_submatrix_sum.py#L51
class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """
    def maxSubmatrix(self, matrix):
        if not matrix or not matrix[0]:
            return 0        
        n_row, n_col = len(matrix), len(matrix[0])
        max_submatrix_sum = float('-inf')
        for top in range(n_row):
            col_sums = [0] * n_col
            for down in range(top, n_row):
                prefix_sum = 0
                prefix_sum_list = []
                for col in range(n_col):
                    col_sums[col] += matrix[down][col]
                    prefix_sum += col_sums[col]
                    prefix_sum_list.append(prefix_sum)
                max_submatrix_sum = max(max_submatrix_sum, self.get_max_diff(prefix_sum_list))
                
        return max_submatrix_sum

    def get_max_diff(self, prefix_sum_list):
        prefix_sum_list_with_zero = [0] + prefix_sum_list
        max_diff = float('-inf')
        min_element = float('inf')
        for prefix_sum in prefix_sum_list_with_zero:
            if prefix_sum < min_element:
                min_element = prefix_sum
                continue
            max_diff = max(prefix_sum - min_element, max_diff)
        return max_diff


        
