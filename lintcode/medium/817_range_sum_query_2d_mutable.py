'''
Link: https://www.lintcode.com/problem/817/
'''


# My own solution. Let each column be a binary indexed tree. We also have padded 0s as the first row and column, respectively.
# Assuming there are n rows and m columns. The update() operation has O(mlogn) time complexity, while sumRegion() has O(logn) time complexity.
# The initialization has O(mnlogn) time complexity.
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # n rows, m columns.
        self.n, self.m = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.bit_trees_for_each_col = [[0] * (self.n + 2) for _ in range(self.m + 1)] 
        for col in range(self.m + 1):
            if col == 0:
                this_column = [0] * (self.n + 1)
            else:
                self.bit_trees_for_each_col[col] = list(self.bit_trees_for_each_col[col - 1])
                this_column = [0]
                for row in range(self.n):
                    this_column.append(matrix[row][col - 1])
            self.initialize_bit_tree(this_column, self.bit_trees_for_each_col[col])

    def initialize_bit_tree(self, array, bit_tree):
        for i in range(len(array)):
            self.add_val_to_affected_entries_in_bit_tree(bit_tree, i, array[i])

    def add_val_to_affected_entries_in_bit_tree(self, bit_tree, idx, diff):
        idx += 1
        while idx < len(bit_tree):
            bit_tree[idx] += diff
            idx += self.get_last_bit(idx)      

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """        
        for col_ind in range(col + 1, self.m + 1):
            self.add_val_to_affected_entries_in_bit_tree(self.bit_trees_for_each_col[col_ind], row + 1, val - self.matrix[row][col])
        self.matrix[row][col] = val
    
    def get_last_bit(self, x):
        return x & (-x)

    def get_prefix_sum_in_bit_tree(self, bit_tree, idx):
        idx += 1
        res = 0
        while idx > 0:
            res += bit_tree[idx]
            idx -= self.get_last_bit(idx)
        return res

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        right_bit_tree, left_bit_tree = self.bit_trees_for_each_col[col2 + 1], self.bit_trees_for_each_col[col1]
        bottom_right = self.get_prefix_sum_in_bit_tree(right_bit_tree, row2 + 1) - self.get_prefix_sum_in_bit_tree(right_bit_tree, row1)
        bottom_left = self.get_prefix_sum_in_bit_tree(left_bit_tree, row2 + 1) - self.get_prefix_sum_in_bit_tree(left_bit_tree, row1)
        return bottom_right - bottom_left
      
      
# My own solution. Let each row be a segment tree. We also have padded 0s as the first row and column, respectively.
# Assuming there are n rows and m columns. The update() operation has O(nlogm) time complexity, while sumRegion() has O(logm) time complexity.
# The initialization has O(nmlogm) time complexity.
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # n rows, m columns.
        self.n, self.m = len(matrix), len(matrix[0])
        self.matrix = matrix
        i = 0
        self.segtree_size = 0
        while True:
            power = 2 ** i
            if power >= self.m + 1:
                self.segtree_size = 2 * power - 1
                break
            i += 1
        self.segtrees_for_each_row = [[0] * (self.segtree_size) for _ in range(self.n + 1)]
        for row_ind in range(self.n + 1):
            if row_ind == 0:
                row = [0] * (self.m + 1)
            else:
                prev_row = row
                curr_row = [0] + matrix[row_ind - 1]
                row = [(x + y) for x, y in zip(prev_row, curr_row)]
            self.construct_segtree(row, self.segtrees_for_each_row[row_ind], 0, self.m, 0)

    def construct_segtree(self, array, segtree, low, high, pos):       
        if low == high:
            segtree[pos] = array[low]
            return
        mid = (low + high) // 2
        self.construct_segtree(array, segtree, low, mid, 2 * pos + 1)
        self.construct_segtree(array, segtree, mid + 1, high, 2 * pos + 2)
        segtree[pos] = segtree[2 * pos + 1] + segtree[2 * pos + 2]  

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """      
        index = col + 1
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        for row_ind in range(row + 1, self.n + 1):
            self.update_segtree(self.segtrees_for_each_row[row_ind], index, diff, 0, self.m, 0)        

    def update_segtree(self, segtree, index, diff, low, high, pos):
        if low > index or high < index:
            return
        if low == high == index:
            segtree[pos] += diff
            return
        mid = (low + high) // 2
        self.update_segtree(segtree, index, diff, low, mid, 2 * pos + 1)
        self.update_segtree(segtree, index, diff, mid + 1, high, 2 * pos + 2)
        segtree[pos] = segtree[2 * pos + 1] + segtree[2 * pos + 2]
           
    def range_sum_query(self, segtree, qlow, qhigh, low, high, pos):
        if low > qhigh or high < qlow:
            return 0
        if low >= qlow and high <= qhigh:
            return segtree[pos]
        mid = (low + high) // 2
        left_range_sum = self.range_sum_query(segtree, qlow, qhigh, low, mid, 2 * pos + 1)
        right_range_sum = self.range_sum_query(segtree, qlow, qhigh, mid + 1, high, 2 * pos + 2)
        return left_range_sum + right_range_sum

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.range_sum_query(self.segtrees_for_each_row[row2 + 1], col1 + 1, col2 + 1, 0, self.m, 0) - \
                self.range_sum_query(self.segtrees_for_each_row[row1], col1 + 1, col2 + 1, 0, self.m, 0)
    
    
    
