'''
Link: https://www.lintcode.com/problem/778/
'''

# My own solution, uses BFS. Should be correct, but hits time limit exceeded error.
from typing import (
    List,
)

from collections import deque
DELTA = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    """
    @param matrix: the given matrix
    @return: The list of grid coordinates
             we will sort your return value in output
    """
    def pacific_atlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        results = []
        if not matrix or not matrix[0]:
            return results
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if self.is_cell_on_ridge(matrix, n, m, i, j):
                    results.append([i, j])
        return results

    def is_cell_on_ridge(self, matrix, n, m, i, j):
        visited = [[False for _ in range(m)] for _ in range(n)]
        queue = deque([(i, j)])
        visited[i][j] = True
        reaches_pacific, reaches_atlantic = False, False
        while queue:
            x, y = queue.popleft()
            prev_height = matrix[x][y]
            if x == 0 or y == 0:
                reaches_pacific = True
            if x == n - 1 or y == m - 1:
                reaches_atlantic = True
            if reaches_atlantic and reaches_pacific:
                return True
            for delta_x, delta_y in DELTA:
                new_x, new_y = x + delta_x, y + delta_y
                if min(new_x, new_y) < 0 or new_x >= n or new_y >= m:
                    continue
                if matrix[new_x][new_y] > prev_height:
                    continue
                if visited[new_x][new_y]:
                    continue
                visited[new_x][new_y] = True
                queue.append((new_x, new_y))
        return False  
      
      
