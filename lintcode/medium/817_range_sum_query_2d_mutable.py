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
    
    # This implementation of update() is different from what I did for a similar problem:
    # https://github.com/simonfqy/SimonfqyGitHub/blob/0c22536dc64d8d940508b2b115c568a410fb04bb/lintcode/medium/840_range_sum_query_mutable.py#L241.
    # This solution here does not use a dictionary which maps the array indices to segtree indices.
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
    
    
# My own solution, but inspired by jiuzhang.com on BIT trees. This one uses 2D segment tree. Should be correct, but unfortunately it 
# hits time limit exceeded exception.
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # n rows, m columns.
        self.n, self.m = len(matrix), len(matrix[0])
        self.matrix = [[0] * self.m for _ in range(self.n)]
        self.segtree_size = self.get_segtree_size(self.n + 1)
        self.row_segtree_size = self.get_segtree_size(self.m + 1)
        self.segtrees = [[0] * (self.row_segtree_size) for _ in range(self.segtree_size)]
        for row in range(self.n):            
            for col in range(self.m):
                self.update(row, col, matrix[row][col])            

    def get_segtree_size(self, num_entries):
        i = 0
        segtree_size = 0
        while True:
            power = 2 ** i
            if power >= num_entries:
                segtree_size = 2 * power - 1
                break
            i += 1
        return segtree_size    

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """     
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self.update_2d_segtree(0, self.n, 0, self.m, row + 1, col + 1, 0, 0, diff)                    

    def update_2d_segtree(self, low_1, high_1, low_2, high_2, row_ind, col_ind, pos_1, pos_2, diff):
        if low_1 > row_ind or high_1 < row_ind:
            return
        if low_1 == high_1 == row_ind:
            self.update_1d_segtree(low_2, high_2, col_ind, pos_1, pos_2, diff)
            return
        mid_1 = (low_1 + high_1) // 2
        self.update_2d_segtree(low_1, mid_1, low_2, high_2, row_ind, col_ind, 2 * pos_1 + 1, pos_2, diff)
        self.update_2d_segtree(mid_1 + 1, high_1, low_2, high_2, row_ind, col_ind, 2 * pos_1 + 2, pos_2, diff)
        # This calculation is elegant but not very efficient.
        self.segtrees[pos_1] = [(x + y) for x, y in zip(self.segtrees[2 * pos_1 + 1], self.segtrees[2 * pos_1 + 2])]

    def update_1d_segtree(self, low, high, ind, pos_1, pos_2, diff):
        if low > ind or high < ind:
            return
        if low == high == ind:
            self.segtrees[pos_1][pos_2] += diff
            return
        mid = (low + high) // 2
        self.update_1d_segtree(low, mid, ind, pos_1, 2 * pos_2 + 1, diff)
        self.update_1d_segtree(mid + 1, high, ind, pos_1, 2 * pos_2 + 2, diff)
        self.segtrees[pos_1][pos_2] = self.segtrees[pos_1][2 * pos_2 + 1] + self.segtrees[pos_1][2 * pos_2 + 2]
           
    def range_sum_query_2d(self, qlow_1, qhigh_1, qlow_2, qhigh_2, low_1, high_1, low_2, high_2, pos_1, pos_2):
        if low_1 > qhigh_1 or high_1 < qlow_1:
            return 0
        if low_1 >= qlow_1 and high_1 <= qhigh_1:
            return self.range_sum_query_1d(qlow_2, qhigh_2, low_2, high_2, pos_1, pos_2)
        mid_1 = (low_1 + high_1) // 2
        left_range_sum = self.range_sum_query_2d(qlow_1, qhigh_1, qlow_2, qhigh_2, low_1, mid_1, low_2, high_2, 2 * pos_1 + 1, pos_2)
        right_range_sum = self.range_sum_query_2d(qlow_1, qhigh_1, qlow_2, qhigh_2, mid_1 + 1, high_1, low_2, high_2, 2 * pos_1 + 2, pos_2)
        return left_range_sum + right_range_sum

    def range_sum_query_1d(self, qlow, qhigh, low, high, pos_1, pos_2):
        if low > qhigh or high < qlow:
            return 0
        if low >= qlow and high <= qhigh:
            return self.segtrees[pos_1][pos_2]
        mid = (low + high) // 2
        left_range_sum = self.range_sum_query_1d(qlow, qhigh, low, mid, pos_1, 2 * pos_2 + 1)
        right_range_sum = self.range_sum_query_1d(qlow, qhigh, mid + 1, high, pos_1, 2 * pos_2 + 2)
        return left_range_sum + right_range_sum

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.range_sum_query_2d(row1 + 1, row2 + 1, col1 + 1, col2 + 1, 0, self.n, 0, self.m, 0, 0)  
    
    
