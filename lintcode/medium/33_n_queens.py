'''
https://www.lintcode.com/problem/33/
'''

# My own solution. Should be correct, but time complexity is too high and cannot pass.
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
            output_strings.append(list(this_solution))
        return output_strings

    def helper(self, n, positions, start_row, inadmissible_coordinates):
        if len(positions) == n:
            self.solutions.append(positions)
            return
        for i in range(n):  
            if i < start_row:
                continue          
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
