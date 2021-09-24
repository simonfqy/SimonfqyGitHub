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
