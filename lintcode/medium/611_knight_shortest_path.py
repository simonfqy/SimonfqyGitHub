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
        if source.x == destination.x and source.y == destination.y and grid[source.x][source.y] == 0:
            return 0
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
    
    
# Solution from jiuzhang.com using bidirectional BFS. More modularized and cleaner than my code above.
from collections import deque
DELTA = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        if not grid or not grid[0]:
            return -1
        if grid[destination.x][destination.y] == 1:
            return -1
        if source.x == destination.x and source.y == destination.y:
            return 0
        forward_queue = deque([(source.x, source.y)])
        forward_visited = set([(source.x, source.y)])
        backward_queue = deque([(destination.x, destination.y)])
        backward_visited = set([(destination.x, destination.y)])
        length = 0
        while forward_queue and backward_queue:
            length += 1
            if self.extend_queue(forward_queue, forward_visited, backward_visited, grid):
                return length
            length += 1
            if self.extend_queue(backward_queue, backward_visited, forward_visited, grid):
                return length
        return -1
    
    def extend_queue(self, queue, visited, opposite_visited, grid):
        size = len(queue)
        for _ in range(size):
            x, y = queue.popleft()
            for delta in DELTA:
                new_x, new_y = x + delta[0], y + delta[1]
                if not self.is_valid(grid, new_x, new_y, visited):
                    continue
                if (new_x, new_y) in opposite_visited:
                    return True
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
        return False

    def is_valid(self, grid, x, y, visited):
        if (x, y) in visited:
            return False
        if min(x, y) < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        return grid[x][y] == 0    
    
    
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
    
    
# My own solution. Using BFS.
from collections import deque
DELTA = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
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
        n, m = len(grid), len(grid[0])
        queue = deque([(source.x, source.y)])
        visited = set([(source.x, source.y)])
        for length in range(n * m):
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                if x == destination.x and y == destination.y:
                    if grid[x][y] == 0:
                        return length
                    return -1
                for delta in DELTA:
                    new_x, new_y = x + delta[0], y + delta[1]
                    if (new_x, new_y) in visited:
                        continue
                    if min(new_x, new_y) < 0 or new_x >= n or new_y >= m:
                        continue
                    if grid[new_x][new_y] == 1:
                        continue
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
        return -1
    
