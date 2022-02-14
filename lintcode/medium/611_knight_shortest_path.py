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
    
    
# My own solution. Uses 2d dynamic programming. Has O(n^2) time complexity. 
DELTA = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        n, m = len(grid), len(grid[0])
        if n <= 0 or m <= 0:
            return -1
        if source.x == destination.x and source.y == destination.y and grid[source.x][source.y] == 0:
            return 0
        # dp[i][j] stores the length of the path from the source to grid[i][j].
        dp = [[float('inf')] * m for _ in range(n)]
        dp[source.x][source.y] = 0
        sources_to_start_from = [source]
        # For de-duplication.
        visited = set([(source.x, source.y)])
        while sources_to_start_from:
            new_sources_to_start_from = []
            for curr_source in sources_to_start_from:
                x, y = curr_source.x, curr_source.y
                for delta in DELTA:
                    new_x, new_y = x + delta[0], y + delta[1]
                    if (new_x, new_y) in visited:
                        continue
                    if min(new_x, new_y) < 0 or new_x >= n or new_y >= m:
                        continue
                    if grid[new_x][new_y] == 1:
                        continue                    
                    if dp[x][y] + 1 < dp[new_x][new_y]:
                        dp[new_x][new_y] = dp[x][y] + 1
                        # Guaranteed to be the shortest if we encounter it for the first time. Returning now is correct.
                        if new_x == destination.x and new_y == destination.y:
                            return dp[new_x][new_y]
                        new_sources_to_start_from.append(Point(new_x, new_y))
                        visited.add((new_x, new_y))

            sources_to_start_from = new_sources_to_start_from
         
        return -1
    
    
    
