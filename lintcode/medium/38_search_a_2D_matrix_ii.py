'''
Link: https://www.lintcode.com/problem/search-a-2d-matrix-ii/description
'''

# This is my own solution.
class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        occurrence = 0
        if matrix is None or not len(matrix) or not len(matrix[0]) or target is None:
            return occurrence
        for i in range(len(matrix)):
            row = matrix[i]
            start, end = 0, len(row) - 1
            while start + 1 < end:
                mid = (start + end) // 2
                if row[mid] < target:
                    start = mid
                else:
                    end = mid
            occurrence += (row[start] == target)
            occurrence += (row[end] == target)
        return occurrence
