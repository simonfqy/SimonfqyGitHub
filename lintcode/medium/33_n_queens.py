'''
https://www.lintcode.com/problem/33/
'''

# My own solution. DFS without memoization. Should be correct, but time complexity is too high and cannot pass.
class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # A list of list of coordinates. Each solution is a list of coordinates of all the queens.
        self.solutions = []
        self.queen_pos_inadmissible_entries = dict()
        self.helper(n, [], 0, set())
        output_strings = []
        for positions in self.solutions:
            this_solution = []
            for i in range(n):
                this_row = ""
                for j in range(n):
                    if (i, j) in positions:
                        this_row += "Q"
                    else:
                        this_row += "."
                this_solution.append(this_row)            
            output_strings.append(this_solution)
        return output_strings

    def helper(self, n, positions, start_row, inadmissible_coordinates):
        if len(positions) == n:
            self.solutions.append(positions)
            return
        for i in range(start_row, n):  
            for j in range(n):
                if (i, j) in inadmissible_coordinates:
                    continue
                updated_inadmissible_coord = set(inadmissible_coordinates)
                updated_inadmissible_coord.update(self.get_inadmissible_coordinates_for_single_queen(i, j, n))
                self.helper(n, positions + [(i, j)], i + 1, updated_inadmissible_coord)
    
    def get_inadmissible_coordinates_for_single_queen(self, row, col, n):
        if (row, col) in self.queen_pos_inadmissible_entries:
            return self.queen_pos_inadmissible_entries[(row, col)]
        coordinates = set()
        for j in range(n):
            coordinates.add((row, j))
            coordinates.add((j, col))
            if j <= row and j <= col:
                coordinates.add((row - j, col - j))
            if row + j < n and col + j < n:
                coordinates.add((row + j, col + j)) 
            if j <= row and col + j < n:
                coordinates.add((row - j, col + j))
            if row + j < n and j <= col:
                coordinates.add((row + j, col - j))       
        self.queen_pos_inadmissible_entries[(row, col)] = coordinates
        return coordinates

# A slight improvement from the previous solution, dramatically improved efficiency and passed the tests.      
class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # A list of list of coordinates. Each solution is a list of coordinates of all the queens.
        self.solutions = []
        self.queen_pos_inadmissible_entries = dict()
        self.helper(n, [], 0, set())
        output_strings = []
        for positions in self.solutions:
            this_solution = []
            for i in range(n):
                this_row = ""
                for j in range(n):
                    if (i, j) in positions:
                        this_row += "Q"
                    else:
                        this_row += "."
                this_solution.append(this_row)            
            output_strings.append(this_solution)
        return output_strings

    # This function is the only place where we made the change.
    def helper(self, n, positions, start_row, inadmissible_coordinates):        
        if len(positions) == n:
            self.solutions.append(positions)
            return
        if start_row >= n:
            return
        # NOTE: this is where the change is about. Instead of traversing through all rows starting from start_row, now we only look at the start_row.
        # It is similar in idea to 
        # https://github.com/simonfqy/SimonfqyGitHub/blob/9e9e86a3a4327b052027252aa222a482ee52e825/lintcode/hard/780_remove_invalid_parentheses.py#L15.
        # In fact, we shouldn't be looking at rows after start_row at all in each recursion.
        for j in range(n):
            if (start_row, j) in inadmissible_coordinates:
                continue
            updated_inadmissible_coord = set(inadmissible_coordinates)
            updated_inadmissible_coord.update(self.get_inadmissible_coordinates_for_single_queen(start_row, j, n))
            self.helper(n, positions + [(start_row, j)], start_row + 1, updated_inadmissible_coord)
    
    def get_inadmissible_coordinates_for_single_queen(self, row, col, n):
        if (row, col) in self.queen_pos_inadmissible_entries:
            return self.queen_pos_inadmissible_entries[(row, col)]
        coordinates = set()
        for j in range(n):
            coordinates.add((row, j))
            coordinates.add((j, col))
            if j <= row and j <= col:
                coordinates.add((row - j, col - j))
            if row + j < n and col + j < n:
                coordinates.add((row + j, col + j)) 
            if j <= row and col + j < n:
                coordinates.add((row - j, col + j))
            if row + j < n and j <= col:
                coordinates.add((row + j, col - j))       
        self.queen_pos_inadmissible_entries[(row, col)] = coordinates
        return coordinates  
    
# BFS with memoization. Faster than the approach above, but not as fast as DFS. Though it uses vastly more memory than the solution above, it still passes.  
from collections import deque
class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # Stores the list of list of coordinates.
        queue = deque([([], set([]))])
        self.queen_pos_to_forbidden_positions = dict()
        self.solutions = []
        while queue:
            queen_positions, forbidden_positions = queue.popleft()
            if len(queen_positions) == n:
                self.construct_solutions(queen_positions, n)
                continue
            if queen_positions:
                last_row = queen_positions[-1][0]
            else:
                last_row = -1
            curr_row = last_row + 1
            for j in range(n):
                if (curr_row, j) in forbidden_positions:
                    continue
                updated_forbidden_positions = set(forbidden_positions)
                updated_forbidden_positions.update(self.get_forbidden_positions_given_queen_pos(n, curr_row, j))
                queue.append((queen_positions + [(curr_row, j)], updated_forbidden_positions))
        return self.solutions
    
    def construct_solutions(self, queen_positions, n):
        solution = []
        for queen_pos in queen_positions:
            this_row = ""
            for j in range(n):
                if queen_pos[1] == j:
                    this_row += "Q"
                else:
                    this_row += "."
            solution.append(this_row)
           
        self.solutions.append(solution)
    
    def get_forbidden_positions_given_queen_pos(self, n, row, col):
        if (row, col) in self.queen_pos_to_forbidden_positions:
            return self.queen_pos_to_forbidden_positions[(row, col)]
        forbidden_positions = set()
        for i in range(n):
            forbidden_positions.add((i, col))
            if row + i < n and col + i < n:
                forbidden_positions.add((row + i, col + i))
            if row + i < n and col - i >= 0:
                forbidden_positions.add((row + i, col - i))
        self.queen_pos_to_forbidden_positions[(row, col)] = forbidden_positions
        return forbidden_positions
