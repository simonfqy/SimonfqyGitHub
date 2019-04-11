'''
Link: https://www.lintcode.com/problem/knight-shortest-path/description
'''

# I used bidirectional BFS. The problem with this question is that, if you directly use
# sets and queues containing Point objects, you will get memory exceeding limit error.
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
from collections import deque
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        if grid is None or len(grid) <= 0 or len(grid[0]) <= 0:
            return -1
        length = 0
        nrows = len(grid)
        ncols = len(grid[0])
        # if grid[destination[0], destination[1]] == 1:
        #     return -1
        source_visited, dest_visited = set([(source.x, source.y)]), set([(destination.x, destination.y)])
        queue_source, queue_dest = deque([(source.x, source.y)]), deque([(destination.x, destination.y)])
        offsets = [[-1, -2], [-2, -1], [1, -2], [-2, 1], [-1, 2], [2, -1], [1, 2], [2, 1]]
        
        while len(queue_source) > 0 and len(queue_dest) > 0:
            size_source_q, size_dest_q = len(queue_source), len(queue_dest)
            length += 1
            for _ in range(size_source_q):
                node_x, node_y = queue_source.popleft()
                if grid[node_x][node_y] == 1:
                    continue
                for offset in offsets:
                    x = node_x + offset[0]
                    y = node_y + offset[1]
                    if (x, y) in dest_visited:
                        return length
                    if x < 0 or x >= nrows:
                        continue
                    if y < 0 or y >= ncols:
                        continue
                    if grid[x][y] == 1:
                        continue
                    if (x, y) in source_visited:
                        continue
                    queue_source.append((x, y))
                    source_visited.add((x, y))
            
            length += 1        
            for _ in range(size_dest_q):
                node_x, node_y = queue_dest.popleft()
                if grid[node_x][node_y] == 1:
                    continue
                for offset in offsets:
                    x = node_x + offset[0]
                    y = node_y + offset[1]
                    this_point = Point(a = x, b = y)
                    if (x, y) in source_visited:
                        return length
                    if x < 0 or x >= nrows:
                        continue
                    if y < 0 or y >= ncols:
                        continue
                    if grid[x][y] == 1:
                        continue
                    if (x, y) in dest_visited:
                        continue
                    queue_dest.append((x, y))
                    dest_visited.add((x, y))
            
        return -1
