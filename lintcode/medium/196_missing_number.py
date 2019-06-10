'''
Link: https://www.lintcode.com/problem/missing-number/description
Challenge: Do it in-place with O(1) extra memory and O(n) time.
'''

# My own solution, uses sorting and binary search. O(nlogn) time complexity, O(1) space.
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        # write your code here
        nums.sort()
        return self.find(nums, 0, len(nums) - 1)
        
    def find(self, nums, left, right):
        while left + 1 < right:
            mid = (left + right) // 2
            if mid == nums[mid]:
                left = mid
            elif mid < nums[mid]:
                right = mid
            else:
                assert False
        if left < nums[left]:
            return left
        if right < nums[right]:
            return right
        if right == nums[right]:
            return right + 1
