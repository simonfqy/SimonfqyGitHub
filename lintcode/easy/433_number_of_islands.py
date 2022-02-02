'''
Link: https://www.lintcode.com/problem/433
'''


# My own solution. Uses BFS to visit each island.
from collections import deque
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        self.delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.n, self.m = len(grid), len(grid[0])
        visited = set()
        island_count = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 0 or (i, j) in visited:
                    continue
                self.explore_island(i, j, grid, visited)
                visited.add((i, j))
                island_count += 1
        return island_count

    def explore_island(self, i, j, grid, visited):
        queue = deque([(i, j)])
        while queue:
            row, col = queue.popleft()
            for delta_x, delta_y in self.delta:
                new_row, new_col = row + delta_x, col + delta_y
                if min(new_row, new_col) < 0 or new_row >= self.n or new_col >= self.m:
                    continue
                if grid[new_row][new_col] == 0:
                    continue
                if (new_row, new_col) in visited:
                    continue
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))

                
