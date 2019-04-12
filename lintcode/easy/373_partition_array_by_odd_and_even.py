'''
Link: https://www.lintcode.com/problem/partition-array-by-odd-and-even/description
'''

# My own solution.
class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        if len(nums) < 2:
            return
        odd_ptr, even_ptr = 0, len(nums) - 1
        while odd_ptr < even_ptr:
            while odd_ptr < even_ptr and nums[odd_ptr] % 2 == 1:
                odd_ptr += 1
            while odd_ptr < even_ptr and nums[even_ptr] % 2 == 0:
                even_ptr -= 1
            if odd_ptr < even_ptr:
                nums[odd_ptr], nums[even_ptr] = nums[even_ptr], nums[odd_ptr]
                even_ptr -= 1
                odd_ptr += 1
        return
