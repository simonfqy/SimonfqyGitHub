'''
Link: https://www.lintcode.com/problem/434
'''


# My own solution. Should be correct, but hits time limit exceeded problem.
# NOTE: Don't directly create Point objects to be added to sets. The sets cannot differentiate Point objects with same x and y and treat them as different.

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
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        land_coords = set()
        island_count = 0
        island_counts = []
        self.delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for point in operators:
            linked = (point.x, point.y) in land_coords
            if not linked:
                for delta_x, delta_y in self.delta:
                    new_x, new_y = point.x + delta_x, point.y + delta_y
                    if min(new_x, new_y) < 0 or new_x >= n or new_y >= m:
                        continue
                    if (new_x, new_y) in land_coords:
                        linked = True
                        break
            land_coords.add((point.x, point.y))
            if not linked:
                island_count += 1
            else:
                island_count = self.count_islands(n, m, land_coords)
            island_counts.append(island_count)
            
        return island_counts

    def count_islands(self, n, m, land_coords):
        island_count = 0
        visited = set()
        for row in range(n):
            for col in range(m):
                if (row, col) not in land_coords:
                    continue
                if (row, col) in visited:
                    continue
                visited.add((row, col))
                self.explore_island(row, col, n, m, land_coords, visited)
                island_count += 1
        return island_count

    def explore_island(self, curr_row, curr_col, n, m, land_coords, visited):        
        queue = deque([(curr_row, curr_col)])
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in self.delta:
                new_x, new_y = x + delta_x, y + delta_y
                if min(new_x, new_y) < 0 or new_x >= n or new_y >= m:
                    continue
                if (new_x, new_y) not in land_coords:
                    continue
                if (new_x, new_y) in visited:
                    continue
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
                

