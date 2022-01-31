'''
Link: https://www.lintcode.com/problem/248
'''


# My own solution. Used sorting + binary search. Passed.
class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        A.sort()
        n = len(A)
        res = []
        for val in queries:
            res.append(self.find_ind_in_array(val, A, 0, n - 1))
        return res

    def find_ind_in_array(self, val, array, start, end):
        if start > end:
            return 0
        left, right = start, end        
        while left + 1 < right:
            mid = (left + right) // 2
            if array[mid] >= val:
                right = mid
            else:
                left = mid            
        if array[left] >= val:
            return left
        if array[right] >= val:
            return right
        return right + 1
      
      
# My own simple solution. Even with the slight optimization of sorting A, it still causes time limit exceeded exception.
class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        res = []
        A.sort()
        for query_val in queries:
            smaller_count = 0
            for val in A:
                if val >= query_val:
                    break
                smaller_count += 1
            res.append(smaller_count)
        return res
    
    
# My own solution using value-based segment tree.
class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        max_unique_nums = 10001
        segtree_size = self.get_segtree_size(max_unique_nums)
        self.segtree = [0] * segtree_size
        smaller_counts = []
        for val in A:
            self.increment_count_in_segtree(val + 1, 0, max_unique_nums - 1, 0)
        for query_val in queries:
            smaller_counts.append(self.get_smaller_count(query_val + 1, 0, max_unique_nums - 1, 0))
        return smaller_counts
    
    def increment_count_in_segtree(self, val, low, high, pos):
        if val < low or val > high:
            return
        if low == high == val:
            self.segtree[pos] += 1
            return
        mid = (low + high) // 2
        self.increment_count_in_segtree(val, low, mid, 2 * pos + 1)
        self.increment_count_in_segtree(val, mid + 1, high, 2 * pos + 2)
        self.segtree[pos] = self.segtree[2 * pos + 1] + self.segtree[2 * pos + 2]

    def get_smaller_count(self, val, low, high, pos):
        if val <= low:
            return 0
        if val > high:
            return self.segtree[pos]
        mid = (low + high) // 2
        left_smaller_count = self.get_smaller_count(val, low, mid, 2 * pos + 1)
        right_smaller_count = self.get_smaller_count(val, mid + 1, high, 2 * pos + 2)
        return left_smaller_count + right_smaller_count

    def get_segtree_size(self, num_entries):
        i = 0
        while True:
            power = 2 ** i
            if num_entries <= power:
                return 2 * power - 1
            i += 1
            
            
# My own solution using value-based Fenwick tree.
class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        self.max_unique_nums = 10001
        self.fenwick_tree = [0] * (self.max_unique_nums + 1)
        smaller_counts = []
        for val in A:
            self.increment_count(val)
        for query_val in queries:
            smaller_counts.append(self.get_smaller_count(query_val))
        return smaller_counts
    
    def increment_count(self, val):
        val += 1
        while val <= self.max_unique_nums:
            self.fenwick_tree[val] += 1
            val += self.get_last_digit(val)

    def get_smaller_count(self, val):
        count = 0
        while val > 0:
            count += self.fenwick_tree[val]
            val -= self.get_last_digit(val)
        return count
    
    def get_last_digit(self, x):
        return x & (-x)
    
    
    
