'''
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
'''

# My own solution. Uses two pointers.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        setter_ind = 0
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if setter_ind < i:
                nums[setter_ind] = nums[i]
            setter_ind += 1
        return setter_ind
      
