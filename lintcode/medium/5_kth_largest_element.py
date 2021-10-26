'''
https://www.lintcode.com/problem/kth-largest-element/description
'''

# My solution, based on the teachings from Jiuzhang.com.
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        length = len(nums)
        if length < n:
            return None
        return self.quick_select(n, nums, 0, length - 1)
        
        
    def quick_select(self, n, nums, start, end):
        # It is guaranteed that start <= n - 1 <= end
        if start == end:
            if n - 1 == start:
                return nums[start]
            return
        
        left, right = start, end
        pivot = nums[(start + end) // 2]
        
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        if left <= n - 1:
            return self.quick_select(n, nums, left, end)
        if right >= n - 1:
            return self.quick_select(n, nums, start, right)
        return nums[n-1]
    
    
# Original solution from jiuzhang.com.
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if not A or k < 1 or k > len(A):
            return None
        return self.partition(A, 0, len(A) - 1, len(A) - k)
        
    def partition(self, nums, start, end, k):
        """
        During the process, it's guaranteed start <= k <= end
        """
        if start == end:
            return nums[k]
            
        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
                
        # left is now bigger than right
        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)
        
        return nums[k]
