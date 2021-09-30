'''
https://www.lintcode.com/problem/132/
'''

# My own solution. Uses DFS.
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        existing_words = []
        for word in words:
            word_found = False
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if self.is_word_exist(board, word, "", i, j, set()):
                        existing_words.append(word)
                        word_found = True
                        break
                if word_found:
                    # Can avoid duplicate words. Also prunes the search tree.
                    break
        return existing_words

    def is_word_exist(self, board, word, word_so_far, start_i, start_j, visited):
        next_char = word[len(word_so_far)]
        if board[start_i][start_j] != next_char:
            return False
        word_so_far += board[start_i][start_j]
        if len(word_so_far) == len(word):
            return True
        new_visited = set(visited)
        new_visited.add((start_i, start_j))
        candidate_positions = [(start_i + 1, start_j), (start_i, start_j - 1), \
            (start_i, start_j + 1), (start_i - 1, start_j)]        
        
        for pos in candidate_positions:
            if pos[0] < 0 or pos[0] >= len(board) or pos[1] < 0 or pos[1] >= len(board[pos[0]]):
                continue 
            if pos in new_visited:
                continue             
            if self.is_word_exist(board, word, word_so_far, pos[0], pos[1], new_visited):
                return True
        return False
