'''
Link: https://www.lintcode.com/problem/search-for-a-range/description
'''

# My own solution.
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        indices = [-1, -1]
        if A is None or target is None or not len(A):
            return indices
        # get the first index
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
            
        if A[start] == target:
            indices[0] = start
        elif A[end] == target:
            indices[0] = end 
        
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > target:
                end = mid
            else:
                start = mid
        if A[end] == target:
            indices[1] = end
        elif A[start] == target:
            indices[1] = start
        
        return indices
