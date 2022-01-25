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
    
    
    
