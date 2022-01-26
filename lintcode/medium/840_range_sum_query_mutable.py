'''
Link: https://www.lintcode.com/problem/840/
'''

# My own solution. It is a straightforward, brute-force solution.
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.nums[i] = val        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i : j + 1])
      
      
# Should be correct, but hits the time limit exceeded exception.
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.prefix_sum = [0] * (len(nums) + 1)        
        for i in range(len(self.nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        for j in range(i + 1, len(self.nums) + 1):
            self.prefix_sum[j] += diff        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefix_sum[j + 1] - self.prefix_sum[i]
    
    
# Also hits the time limit exceeded exception. The bad thing about this algorithm is that, sumRange() time complexity depends on the number
# of update() operations executed.
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.index_to_diff = dict()
        self.prefix_sum = [0] * (len(nums) + 1)        
        for i in range(len(self.nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        aggregated_diff = val - self.nums[i]
        self.nums[i] = val
        if i in self.index_to_diff:
            aggregated_diff = self.index_to_diff[i] + aggregated_diff
            if aggregated_diff == 0:
                del self.index_to_diff[i]
                return
        self.index_to_diff[i] = aggregated_diff

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        original_sum = self.prefix_sum[j + 1] - self.prefix_sum[i]
        for ind, diff in sorted(self.index_to_diff.items()):
            if ind < i:
                continue
            if ind > j:
                break
            original_sum += diff
        return original_sum
    
    
# My implementation based on the solution from jiuzhang.com. It uses binary index tree (also called Fenwick tree), which has O(logn) time complexity
# on both update() and prefix sum operations. 
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.n = len(self.nums)
        self.binary_index_tree_array = [0] * (self.n + 1)
        for i in range(self.n):
            self.add_val_to_all_affected_entries(i, self.nums[i])             
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        self.add_val_to_all_affected_entries(i, diff)

    def get_lowest_bit(self, x):
        return x & (-x)

    def add_val_to_all_affected_entries(self, index, val):
        index += 1
        while index <= self.n:
            self.binary_index_tree_array[index] += val
            index += self.get_lowest_bit(index)
    
    def get_prefix_sum(self, index):
        index += 1
        prefix_sum = 0
        while index > 0:
            prefix_sum += self.binary_index_tree_array[index]
            index -= self.get_lowest_bit(index)
        return prefix_sum    

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.get_prefix_sum(j) - self.get_prefix_sum(i - 1)
    
    
# My implementation based on a solution from a student on jiuzhang.com. It uses segment tree, which has O(logn) time complexity.
# The implementation of sumRange() function is not very intuitive. 
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.segment_tree_arr = [0] * self.n + nums
        for i in range(self.n - 1, 0, -1):
            # i's sons are 2i, 2i + 1
            self.segment_tree_arr[i] = self.segment_tree_arr[i << 1] + self.segment_tree_arr[i << 1 | 1]                   
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        index = i + self.n
        diff = val - self.segment_tree_arr[index]        
        while index > 0:
            self.segment_tree_arr[index] += diff
            # This line below is also okay if we don't use diff: if i is odd, left is i - 1, if i is even, right is i + 1
            # self.tree_arr[i >> 1] = self.tree_arr[i] + self.tree_arr[i ^ 1]
            index >>= 1   
    
    # To help understand the problem, we can let self.n = 8, i = 3, j = 6. 
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        l, r = i + self.n, j + self.n
        res = 0
        while l <= r:
            # It means l = 2k + 1 for some k. Let l = (l + 1) >> 1, then l becomes k + 1.
            if l & 1:
                res += self.segment_tree_arr[l]
                l += 1
            l >>= 1
            # It means r = 2m for some m, where m > k. Let r = (r - 1) >> 1, then r becomes m - 1. The values of r and l are likely to get closer (if not already
            # passing each other) after this iteration of the while loop.
            if not r & 1:
                res += self.segment_tree_arr[r]
                r -= 1
            r >>= 1
        return res
    
    
