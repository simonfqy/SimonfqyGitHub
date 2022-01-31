'''
Link: https://www.lintcode.com/problem/249/
'''


# My own solution which uses segment tree. Should be correct, but hits time limit exceeded exception.
class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def countOfSmallerNumberII(self, A):
        n = len(A)
        segtree_size = self.get_segtree_size(n)
        self.segtree = [(float('inf'), float('-inf'))] * segtree_size
        smaller_counts = []
        for i in range(n):
            smaller_counts.append(self.get_smaller_element_count(A[i], i, 0, n - 1, 0))
            self.update_segtree(A, i, 0, n - 1, 0)
        return smaller_counts

    def update_segtree(self, array, index, low, high, pos):
        if low > index or high < index:
            return
        if low == high == index:
            self.segtree[pos] = (array[low], array[low])
            return
        mid = (low + high) // 2
        self.update_segtree(array, index, low, mid, 2 * pos + 1)
        self.update_segtree(array, index, mid + 1, high, 2 * pos + 2)
        self.segtree[pos] = (min(self.segtree[2 * pos + 1][0], self.segtree[2 * pos + 2][0]), 
                max(self.segtree[2 * pos + 1][1], self.segtree[2 * pos + 2][1]))

    def get_smaller_element_count(self, val, index, low, high, pos):
        min_val, max_val = self.segtree[pos]
        if low >= index:
            return 0
        if min_val >= val:
            return 0
        if max_val < val and high < index:
            return high - low + 1
        mid = (low + high) // 2
        left_smaller_count = self.get_smaller_element_count(val, index, low, mid, 2 * pos + 1)
        right_smaller_count = self.get_smaller_element_count(val, index, mid + 1, high, 2 * pos + 2)
        return left_smaller_count + right_smaller_count
    
    def get_segtree_size(self, num_entries):
        i = 0
        while True:
            power = 2 ** i
            if power >= num_entries:
                return 2 * power - 1
            i += 1
            
            
# My own implementation using Binary Indexed Tree (Fenwick Tree). Should be correct, but also hits time limit exceeded exception.
class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def countOfSmallerNumberII(self, A):
        self.n = len(A)
        self.fenwick_tree = [(float('inf'), float('-inf'))] * (self.n + 1)
        counts = []
        for i, val in enumerate(A):
            counts.append(self.get_num_smaller_numbers(A, i, val))
            self.update(i, val)
        return counts

    def update(self, index, val):
        index += 1
        while index <= self.n:
            self.fenwick_tree[index] = (min(self.fenwick_tree[index][0], val), max(self.fenwick_tree[index][1], val))
            index += self.get_last_digit(index)

    def get_num_smaller_numbers(self, array, index, val):        
        if index <= 0:
            return 0
        smaller_count = 0
        min_val, max_val = self.fenwick_tree[index]
        decrement = self.get_last_digit(index)
        if max_val < val:
            smaller_count += decrement
        elif min_val < val:
            prev_ind = index - 1
            smaller_count = self.get_num_smaller_numbers(array, prev_ind, val)
            smaller_count += (array[index - 1] < val)
            return smaller_count

        index -= decrement
        smaller_count += self.get_num_smaller_numbers(array, index, val)
        return smaller_count
    
    def get_last_digit(self, x):
        return x & (-x)
    
  
