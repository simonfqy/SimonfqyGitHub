'''
Link: https://www.lintcode.com/problem/123/
'''

# My own solution. Should be correct, but it hits the time limit exceeded exception.
from typing import (
    List,
)

DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        # write your code here
        if not board or not board[0]:
            return False
        n = len(board)
        m = len(board[0])
        visited = set()
        for i in range(n):
            for j in range(m):
                if self.is_correct_word(board, i, j, word, visited | {(i, j)}):
                    return True
        return False
    
    def is_correct_word(self, board, i, j, word, visited):
        if word == "":
            return True
        if board[i][j] != word[0]:
            return False
        for delta_x, delta_y in DELTA:
            new_x, new_y = i + delta_x, j + delta_y
            if min(new_x, new_y) < 0 or new_x >= len(board) or new_y >= len(board[0]):
                continue
            if (new_x, new_y) in visited:
                continue
            if self.is_correct_word(board, new_x, new_y, word[1:], visited | {(new_x, new_y)}):
                return True
        return False
      

# My own solution. Though it is similar to the one above, this one doesn't encounter time limit exceeded error.
# Nevertheless, the space consumption was a bit large.
DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        # write your code here
        if not board or not board[0]:
            return False
        n = len(board)
        m = len(board[0])
        visited = set()
        for i in range(n):
            for j in range(m):
                if board[i][j] != word[0]:
                    continue
                if self.is_correct_word(board, i, j, word[1:], {(i, j)}):
                    return True
        return False
    
    def is_correct_word(self, board, i, j, word, visited):
        if word == "":
            return True
        for delta_x, delta_y in DELTA:
            new_x, new_y = i + delta_x, j + delta_y
            if min(new_x, new_y) < 0 or new_x >= len(board) or new_y >= len(board[0]):
                continue
            if board[new_x][new_y] != word[0] or (new_x, new_y) in visited:
                continue
            if self.is_correct_word(board, new_x, new_y, word[1:], visited | {(new_x, new_y)}):
                return True
        return False
  

# My implementation of the solution on jiuzhang.com. Uses 2D array rather than a set to store the visited entries.
# Requires explicit resetting to False. Has less space consumption and takes slightly less time than the solution above.
DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        # write your code here
        if not board or not board[0]:
            return False
        n = len(board)
        m = len(board[0])
        self.visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] != word[0]:
                    continue
                self.visited[i][j] = True
                if self.is_correct_word(board, i, j, word[1:]):
                    return True
                self.visited[i][j] = False
        return False
    
    def is_correct_word(self, board, i, j, word):
        if word == "":
            return True
        for delta_x, delta_y in DELTA:
            new_x, new_y = i + delta_x, j + delta_y
            if min(new_x, new_y) < 0 or new_x >= len(board) or new_y >= len(board[0]):
                continue
            if self.visited[new_x][new_y] or board[new_x][new_y] != word[0]:
                continue
            self.visited[new_x][new_y] = True
            if self.is_correct_word(board, new_x, new_y, word[1:]):
                return True
            # Backtracking: resetting flag value to False.
            self.visited[new_x][new_y] = False
        return False
