'''
Link: https://www.lintcode.com/problem/943/
'''


# My own solution, using prefix sum.
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix_sums = [0]
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            self.prefix_sums.append(prefix_sum)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefix_sums[j + 1] - self.prefix_sums[i]
      
      
