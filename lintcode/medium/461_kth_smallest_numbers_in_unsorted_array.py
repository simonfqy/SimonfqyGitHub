'''
Link: https://www.lintcode.com/problem/kth-smallest-numbers-in-unsorted-array/description
'''

# My own solution after some painstaking debugging process.
class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        if k > len(nums) or k < 1:
            return None
        left, right = 0, len(nums) - 1
        return self.quick_select(k - 1, nums, left, right)
        
        
    def quick_select(self, k, nums, start, end):
        left, right = start, end
        # Initially I set the following to right - left <= 1, which would occasionally return wrong results.
        if right <= left:
            return nums[k]
        pivot = nums[(left + right) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            # Initially I set the second condition to nums[right] >= pivot, which could cause infinite loop
            # if we have k = 3 and [3, 4, 1, 2, 5] as the input. So we must have > or <, no =.
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
        if k <= right:
            return self.quick_select(k, nums, start, right)
        if k >= left:
            return self.quick_select(k, nums, left, end)
        return nums[k]
