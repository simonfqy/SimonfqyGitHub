'''
Link: https://www.lintcode.com/problem/248
'''


# My own solution. Used sorting + binary search.
class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        A.sort()
        n = len(A)
        res = []
        for val in queries:
            res.append(self.find_ind_in_array(val, A, 0, n - 1))
        return res

    def find_ind_in_array(self, val, array, start, end):
        if start > end:
            return 0
        left, right = start, end        
        while left + 1 < right:
            mid = (left + right) // 2
            if array[mid] >= val:
                right = mid
            else:
                left = mid            
        if array[left] >= val:
            return left
        if array[right] >= val:
            return right
        return right + 1
      
      