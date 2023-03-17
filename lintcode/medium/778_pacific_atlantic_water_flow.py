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
      
      
# My solution based on the teachings from jiuzhang.com. Performing BFS from the edges to the centre, and taking
# intersection at the end.
from collections import deque
DELTA = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    """
    @param matrix: the given matrix
    @return: The list of grid coordinates
             we will sort your return value in output
    """
    def pacific_atlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        atlantic_sources = set()
        pacific_sources = set()
        if not matrix or not matrix[0]:
            return []
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    self.get_water_source(matrix, n, m, i, j, atlantic_sources)
                if i == n - 1 or j == m - 1:
                    self.get_water_source(matrix, n, m, i, j, pacific_sources)
        results_set = atlantic_sources & pacific_sources
        return [list(tup) for tup in results_set]

    def get_water_source(self, matrix, n, m, i, j, water_source):
        visited = [[False for _ in range(m)] for _ in range(n)]
        queue = deque([(i, j)])
        visited[i][j] = True
        water_source.add((i, j))
        while queue:
            x, y = queue.popleft()
            prev_height = matrix[x][y]
            for delta_x, delta_y in DELTA:
                new_x, new_y = x + delta_x, y + delta_y
                if min(new_x, new_y) < 0 or new_x >= n or new_y >= m:
                    continue
                if matrix[new_x][new_y] < prev_height:
                    continue
                if visited[new_x][new_y] or (new_x, new_y) in water_source:
                    continue
                visited[new_x][new_y] = True
                water_source.add((new_x, new_y))
                queue.append((new_x, new_y))  
                
   
# My own solution based on the teachings from jiuzhang.com. Taking DFS from edges to the centre.
DELTA = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    """
    @param matrix: the given matrix
    @return: The list of grid coordinates
             we will sort your return value in output
    """
    def pacific_atlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        atlantic_sources = set()
        pacific_sources = set()
        if not matrix or not matrix[0]:
            return []
        n, m = len(matrix), len(matrix[0])
        atlantic_visited = [[False for _ in range(m)] for _ in range(n)]
        pacific_visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    atlantic_visited[i][j] = True
                    self.get_water_source(matrix, n, m, i, j, atlantic_sources, atlantic_visited)
                    atlantic_visited[i][j] = False
                if i == n - 1 or j == m - 1:
                    pacific_visited[i][j] = True
                    self.get_water_source(matrix, n, m, i, j, pacific_sources, pacific_visited)
                    pacific_visited[i][j] = False
        results_set = atlantic_sources & pacific_sources
        return [list(tup) for tup in results_set]

    def get_water_source(self, matrix, n, m, i, j, water_source, visited):
        water_source.add((i, j))       
        prev_height = matrix[i][j]
        for delta_x, delta_y in DELTA:
            new_x, new_y = i + delta_x, j + delta_y
            if min(new_x, new_y) < 0 or new_x >= n or new_y >= m:
                continue
            if matrix[new_x][new_y] < prev_height:
                continue
            if visited[new_x][new_y] or (new_x, new_y) in water_source:
                continue
            visited[new_x][new_y] = True
            self.get_water_source(matrix, n, m, new_x, new_y, water_source, visited)
            visited[new_x][new_y] = False 
            
           
# Simplified solution based on the one above, learned from jiuzhang.com. Here we can remove the visited flag
# 2D array and simply use the water_source set for pruning.
DELTA = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    """
    @param matrix: the given matrix
    @return: The list of grid coordinates
             we will sort your return value in output
    """
    def pacific_atlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        atlantic_sources = set()
        pacific_sources = set()
        if not matrix or not matrix[0]:
            return []
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    self.get_water_source(matrix, n, m, i, j, atlantic_sources)
                if i == n - 1 or j == m - 1:
                    self.get_water_source(matrix, n, m, i, j, pacific_sources)
        results_set = atlantic_sources & pacific_sources
        return [list(tup) for tup in results_set]

    def get_water_source(self, matrix, n, m, i, j, water_source):
        water_source.add((i, j))       
        prev_height = matrix[i][j]
        for delta_x, delta_y in DELTA:
            new_x, new_y = i + delta_x, j + delta_y
            if min(new_x, new_y) < 0 or new_x >= n or new_y >= m:
                continue
            if matrix[new_x][new_y] < prev_height:
                continue
            if (new_x, new_y) in water_source:
                continue
            self.get_water_source(matrix, n, m, new_x, new_y, water_source)
            
            
