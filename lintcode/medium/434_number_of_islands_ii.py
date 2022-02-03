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
        for (row, col) in land_coords:
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
                if (new_x, new_y) not in land_coords:
                    continue
                if min(new_x, new_y) < 0 or new_x >= n or new_y >= m:
                    continue
                if (new_x, new_y) in visited:
                    continue
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
                

# My own solution. Should be correct, but also hits time limit exceeded problem.
from collections import deque
class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        island_counts = []
        islands = deque()
        self.delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for point in operators:                
            self.update_islands(point, islands)                   
            island_counts.append(len(islands))
            
        return island_counts
        
    def update_islands(self, point, islands):
        affected_island_inds = set()
        expanded_island = set([(point.x, point.y)])      
        max_affected_island_ind = -1   
        for i, island in enumerate(islands):
            if (point.x, point.y) in island:
                return
            for delta_x, delta_y in self.delta:
                new_x, new_y = point.x + delta_x, point.y + delta_y                
                if (new_x, new_y) not in island:
                    continue             
                expanded_island |= island
                affected_island_inds.add(i)
                max_affected_island_ind = i
                break
        
        for i in range(len(islands)):
            if i > max_affected_island_ind:
                break
            island = islands.popleft()            
            if i in affected_island_inds:
                continue            
            islands.append(island)
        islands.appendleft(expanded_island)


# This solution also hits the time limit exceeded problem.
class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        island_counts = []
        island_ind_to_island = dict()
        coord_to_island_ind = dict()
        self.delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for point in operators:                
            self.update_islands(point, island_ind_to_island, coord_to_island_ind)                   
            island_counts.append(len(island_ind_to_island))
            
        return island_counts
        
    def update_islands(self, point, island_ind_to_island, coord_to_island_ind):
        if (point.x, point.y) in coord_to_island_ind:
            return
        expanded_island = set([(point.x, point.y)])
        if island_ind_to_island:      
            smallest_available_ind = max(island_ind_to_island) + 1
        else:
            smallest_available_ind = 0
        affected_island_inds = set()
        
        for delta_x, delta_y in self.delta:
            new_x, new_y = point.x + delta_x, point.y + delta_y                
            if (new_x, new_y) not in coord_to_island_ind:
                continue             
            island_ind = coord_to_island_ind[(new_x, new_y)]
            expanded_island |= island_ind_to_island[island_ind]  
            affected_island_inds.add(island_ind)             
            
        for ind in affected_island_inds:            
            smallest_available_ind = min(smallest_available_ind, ind)
            del island_ind_to_island[ind]
        
        island_ind_to_island[smallest_available_ind] = expanded_island
        for row, col in expanded_island:
            coord_to_island_ind[(row, col)] = smallest_available_ind               

            
