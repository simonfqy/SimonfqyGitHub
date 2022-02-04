'''
Link: https://www.lintcode.com/problem/654/
'''


# My own solution. It's a straightforward multiplication with some optimization to skip fully zero A rows or B columns.
class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        a_rows, a_cols = len(A), len(A[0])
        b_rows, b_cols = len(B), len(B[0])
        res = [[0] * b_cols for _ in range(a_rows)]        
        self.all_zero_B_cols = set()
        for row_ind in range(a_rows):            
            self.multiply_A_row_to_B(A[row_ind], B, b_cols, res[row_ind])
        return res

    def multiply_A_row_to_B(self, A_row, B, b_cols, result_row):
        A_row_is_all_zero = False
        for col_ind in range(b_cols):
            summ = 0
            if A_row_is_all_zero or col_ind in self.all_zero_B_cols:
                result_row[col_ind] = summ
                continue
            self.all_zero_B_cols.add(col_ind)
            A_row_is_all_zero = True
            for i, a_element in enumerate(A_row):
                if B[i][col_ind] != 0 and col_ind in self.all_zero_B_cols:
                    self.all_zero_B_cols.remove(col_ind)
                if a_element == 0:
                    continue
                A_row_is_all_zero = False                
                if B[i][col_ind] == 0:
                    continue                
                summ += a_element * B[i][col_ind]
            result_row[col_ind] = summ
            
            
