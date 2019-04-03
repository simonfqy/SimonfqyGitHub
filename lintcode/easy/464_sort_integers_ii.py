'''
Link: https://www.lintcode.com/problem/sort-integers-ii/description
'''

# This is copied from the teachings of Jiuzhang.com. Other versions of quick sort do exist.
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        self.quick_sort(A, 0, len(A) - 1)
        
        
    def quick_sort(self, A, start, end):
        if start >= end:
            return
        pivot = A[(start + end) // 2]
        left, right = start, end
        
        # Here we need to have left <= right in this while block. Because if we do not,
        # we would cause overlapping portions in left and right sorted subarrays, and stackoverflow.
        while left <= right:
            # If an array is composed of the same values, then it would undergo O(n) swaps and result
            # in two sorted subarrays with similar size. The swapping seems to be unnecessary, but if
            # we avoid swapping by setting the conditions to be A[left] <= pivot and A[right] >= pivot,
            # it would result in left == right + 1, and right unchanged. Thus it would cause stack overflow
            # error. So we must set the conditions to be A[left] < pivot and A[right] > pivot, at the
            # expense of 'unnecessary' swaps.
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
                
        self.quick_sort(A, start, right)
        self.quick_sort(A, left, end)
