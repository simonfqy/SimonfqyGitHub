'''
Link: https://www.lintcode.com/problem/classical-binary-search/description
The implementations are based on the template provided in:
https://github.com/simonfqy/SimonfqyGitHub/blob/e22a5e2fe5872c9525d2ba34c7d3bf7c9015f6eb/algorithms/binary_search.py#L8
'''

# This solution returns the first occurrence of the target.
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if nums is None or not len(nums):
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if target > nums[mid]:
                start = mid
            elif target == nums[mid]:
                # We are trying to find the first occurrence
                end = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
        
# This solution returns the last occurrence of the target.
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if not nums or not len(nums):
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end)//2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1
