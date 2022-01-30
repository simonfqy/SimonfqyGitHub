'''
Link: https://www.lintcode.com/problem/249/
'''


# My own solution. Should be correct, but hits time limit exceeded exception.
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
            
            
