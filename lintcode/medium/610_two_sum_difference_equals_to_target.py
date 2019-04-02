'''
Link: https://www.lintcode.com/problem/two-sum-difference-equals-to-target/description
'''

# My own solution.
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        num_to_ind = dict()
        for i, num in enumerate(nums):
            if num - target in num_to_ind:
                return [num_to_ind[num - target] + 1, i + 1]
            if num + target in num_to_ind:
                return [num_to_ind[num + target] + 1, i + 1]
            num_to_ind[num] = i
