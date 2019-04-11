'''
Link: https://www.lintcode.com/problem/knight-shortest-path-ii/description
'''

# Using unidirectional BFS.
from collections import deque
class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        if grid is None or len(grid) <= 0 or len(grid[0]) <= 0:
            return -1
        nrow = len(grid)
        ncol = len(grid[0])
        length = 0
        offsets = [[1, 2], [-1, 2], [2, 1], [-2, 1]]
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        dest = (nrow - 1, ncol - 1)
        while queue:
            size_queue = len(queue)
            length += 1
            for _ in range(size_queue):
                node_x, node_y = queue.popleft()
                if not self.is_valid(grid, node_x, node_y, nrow, ncol):
                    continue
                for offset in offsets:
                    x = node_x + offset[0]
                    y = node_y + offset[1]
                    if not self.is_valid(grid, x, y, nrow, ncol):
                        continue
                    if (x, y) in visited:
                        continue
                    if x == dest[0] and y == dest[1]:
                        return length
                    queue.append((x, y))
                    visited.add((x, y))
            
        return -1
        
        
    def is_valid(self, grid, x, y, nrow, ncol):
        
        if x < 0 or x >= nrow or y < 0 or y >= ncol:
            return False
        
        return not grid[x][y]
