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
                

# UnionFind solution from jiuzhang.com.
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    ans = 0
    pre = []
    
    def unionfind(self, root):
	    son = root;
	    while(root != self.pre[root]):
	    	root = self.pre[root]
	    while(son != root):
		    tmp = self.pre[son];
		    self.pre[son] = root
		    son = tmp
	    return root
    
    def connect(self, A, B):
        rootA = self.unionfind(A)
        rootB = self.unionfind(B)
        if(rootA != rootB):
            self.pre[rootB] = rootA
            self.ans -= 1
    
    def numIslands(self, grid):
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        self.pre = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.pre += [i * m + j]
                if grid[i][j]:
                    self.ans += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    # Only need to consider the lower and righter neighbor of the current position, because the upper and left neighbors are visited.
                    if(i + 1 < n and grid[i + 1][j]):
                        self.connect(i * m + j + m, i * m + j)
                    if(j + 1 < m and grid[i][j + 1]):
                        self.connect(i * m + j + 1, i * m + j)
        return self.ans

    
