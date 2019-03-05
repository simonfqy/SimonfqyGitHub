'''
Link: https://www.lintcode.com/problem/first-position-of-target/description
'''

# I am using recursion to solve the problem.
class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        if not nums or not len(nums):
            return -1
        return self.bin_search(nums, 0, len(nums) - 1, target)
    
    def bin_search(self, nums, start, end, target):
        if end - start <= 1:
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            return -1
        mid = (start + end) // 2
        if nums[mid] < target:
            return self.bin_search(nums, mid, end, target)
        if nums[mid] == target:
            return self.bin_search(nums, start, mid, target)
        if nums[mid] > target:
            return self.bin_search(nums, start, mid, target)
