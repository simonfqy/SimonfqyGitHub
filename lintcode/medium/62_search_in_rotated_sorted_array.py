'''
Link: https://www.lintcode.com/problem/search-in-rotated-sorted-array/description
'''

# This is my own implementation.
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if A is None or not len(A):
            return -1
        
        # Idea: first get the index of the lowest value, then do binary search in the two segments.
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > A[start]:
                start = mid
            else:
                end = mid
                
        if A[start] < A[end]:
            ind_smallest_value = start
        else:
            ind_smallest_value = end
        
        ind_return = self.binary_search(A, target, ind_smallest_value, len(A) - 1)
        if ind_return != -1:
            return ind_return
        if ind_smallest_value > 0:
            ind_return = self.binary_search(A, target, 0, ind_smallest_value - 1)
        return ind_return
        
        
    def binary_search(self, A, target, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > target:
                end = mid
            elif A[mid] == target:
                return mid
            else:
                start = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
