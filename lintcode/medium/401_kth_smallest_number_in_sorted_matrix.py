'''
Link: https://www.lintcode.com/problem/401/
'''

# My own solution, using heap and a set of visited coordinates. Has very good performance. Time complexity is O(klogn),
# where n is the maximum of the width and height of the matrix.
import heapq
class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        if not matrix or k < 1 or not matrix[0]:
            return None
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        counter = 0
        heap = [(matrix[0][0], 0, 0)]
        visited_coords = set([(0, 0)])
        while heap:
            val, row, col = heapq.heappop(heap)
            counter += 1            
            if counter == k:
                return val
            if row + 1 < num_rows and (row + 1, col) not in visited_coords:
                visited_coords.add((row + 1, col))
                heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))
            if col + 1 < num_cols and (row, col + 1) not in visited_coords:
                visited_coords.add((row, col + 1))
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))

        return None
