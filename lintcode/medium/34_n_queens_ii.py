'''
https://www.lintcode.com/problem/34/
'''

# My own solution. DFS, very similar to the N queens question, just simplified. We only need to keep count.
class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        self.queen_pos_to_forbidden_positions = dict()
        self.solutions_count = 0
        self.helper(n, 0, [], set([]))
        return self.solutions_count

    def helper(self, n, current_row, queen_positions, forbidden_positions):
        if len(queen_positions) == n:
            self.solutions_count += 1
            return
        for j in range(n):
            if (current_row, j) in forbidden_positions:
                continue
            updated_forbidden_pos = set(forbidden_positions)
            updated_forbidden_pos.update(self.get_forbidden_positions_based_on_queen_pos(n, current_row, j))
            self.helper(n, current_row + 1, queen_positions + [(current_row, j)], updated_forbidden_pos)
            
    # An alternative way. Instead of using traversal and increment a global counter, here we divide-and-conquer and let each
    # recursion return a result.
    def helper2(self, n, current_row, queen_positions, forbidden_positions):
        if len(queen_positions) == n:
            return 1
        solution_count = 0
        for j in range(n):
            if (current_row, j) in forbidden_positions:
                continue
            updated_forbidden_pos = set(forbidden_positions)
            updated_forbidden_pos.update(self.get_forbidden_positions_based_on_queen_pos(n, current_row, j))
            solution_count += self.helper(n, current_row + 1, queen_positions + [(current_row, j)], updated_forbidden_pos)
        return solution_count

    def get_forbidden_positions_based_on_queen_pos(self, n, row, col):
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
    
    
# My own solution based on https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/hui-su-sua-c26da/.    
class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        self.results = 0
        self.helper(n, [])
        return self.results

    def helper(self, n, col_list):
        if len(col_list) == n:
            self.results += 1
            return
        row = len(col_list)
        for col in range(n):
            if not self.is_valid_arrangement(n, row, col, col_list):
                continue
            self.helper(n, col_list + [col])

    def is_valid_arrangement(self, n, row, col, col_list):
        for r, c in enumerate(col_list):
            if col == c:
                return False
            if r + c == row + col or r - c == row - col:
                return False
        return True
    
