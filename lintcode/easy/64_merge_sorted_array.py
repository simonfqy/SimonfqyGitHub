'''
Link: https://www.lintcode.com/problem/64/
'''


# My own solution. Has O(mn) time complexity.
class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        i = j = 0

        while i < m + j and j < n:
            if A[i] > B[j]:
                # Move the trailing zeroes to the index i.
                A.insert(i, A.pop())
                A[i] = B[j]
                j += 1
            i += 1                
            
        for ind_B in range(j, n):
            A.insert(i, A.pop())
            A[i] = B[ind_B]
            i += 1
        
