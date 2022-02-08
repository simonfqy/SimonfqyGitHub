'''
https://www.lintcode.com/problem/115/
'''

# My own solution. Uses memoized search.
class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        self.grid_cell_to_path = [[None] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        self.unique_paths(obstacleGrid, 0, 0)
        return self.grid_cell_to_path[0][0]

    def unique_paths(self, obstacleGrid, row, col):
        if self.grid_cell_to_path[row][col] is not None:
            return        
        if obstacleGrid[row][col] == 1:
            self.grid_cell_to_path[row][col] = 0
            return
        if row == len(obstacleGrid) - 1 and col == len(obstacleGrid[0]) - 1:
            self.grid_cell_to_path[row][col] = 1
            return      
        self.grid_cell_to_path[row][col] = 0
        if row + 1 < len(obstacleGrid):
            self.unique_paths(obstacleGrid, row + 1, col)
            self.grid_cell_to_path[row][col] += self.grid_cell_to_path[row + 1][col]
        if col + 1 < len(obstacleGrid[0]):
            self.unique_paths(obstacleGrid, row, col + 1)
            self.grid_cell_to_path[row][col] += self.grid_cell_to_path[row][col + 1]

            
# Slightly modified the solution above. Now the unique_paths() function directly returns the number of paths.
class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        self.grid_cell_to_path = [[None] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        return self.unique_paths(obstacleGrid, 0, 0)         

    def unique_paths(self, obstacleGrid, row, col):
        if row >= len(obstacleGrid) or col >= len(obstacleGrid[0]): 
            return 0
        if self.grid_cell_to_path[row][col] is not None:
            return self.grid_cell_to_path[row][col]       
        if obstacleGrid[row][col] == 1:
            self.grid_cell_to_path[row][col] = 0
            return 0
        if row == len(obstacleGrid) - 1 and col == len(obstacleGrid[0]) - 1:
            self.grid_cell_to_path[row][col] = 1
            return 1
                    
        self.grid_cell_to_path[row][col] = self.unique_paths(obstacleGrid, row + 1, col) + self.unique_paths(obstacleGrid, row, col + 1)        
        return self.grid_cell_to_path[row][col]
    
    
# Dynamic programming solution. The dp cells are the same as the one in memoized search solution.
class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        self.grid_cell_to_paths = [[0] * m for _ in range(n)]
        self.populate_cells(obstacleGrid, n, m)
        return self.grid_cell_to_paths[0][0]         

    def populate_cells(self, obstacleGrid, n, m):
        if obstacleGrid[n - 1][m - 1] == 1:
            return
        self.grid_cell_to_paths[n - 1][m - 1] = 1
        for row in range(n - 1, -1, -1):
            for col in range(m - 1, -1, -1):
                if row == n - 1 and col == m - 1:
                    continue
                if obstacleGrid[row][col] == 1:
                    continue                
                if row < n - 1: 
                    self.grid_cell_to_paths[row][col] = self.grid_cell_to_paths[row + 1][col]
                    if col < m - 1:
                        self.grid_cell_to_paths[row][col] += self.grid_cell_to_paths[row][col + 1]
                    continue
                # Now, row == n - 1 and col < m - 1
                self.grid_cell_to_paths[row][col] = self.grid_cell_to_paths[row][col + 1]
                
                
