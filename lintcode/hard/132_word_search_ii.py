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
    
    # The board[start_i][start_j] character is not yet added to the end of the word_so_far argument. We'll see whether it matches and then
    # add it to word_so_far string if there is a match. Afterwards, we start from (start_i, start_j) to examine its neighbors.
    # This logic is not as natural as the solution below, where word_so_far + board[pos[0]][pos[1]] is passed as the word_so_far parameter 
    # when invoking the is_word_exist() function recursively on neighbors.
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
    
    
# Essentially the same as the solution above. The difference is that, here in is_word_exist() function, the board[start_i][start_j]
# character is already added to the end of the word_so_far string. This slightly reduces the lines of code and makes the logic more natural.
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
                    if self.is_word_exist(board, word, board[i][j], i, j, set()):
                        existing_words.append(word)
                        word_found = True
                        break
                if word_found:
                    break
        return existing_words
    
    # Here the board[start_i][start_j] character is already added to the end of the word_so_far string. We start from (start_i, start_j)
    # to examine its neighbors.
    def is_word_exist(self, board, word, word_so_far, start_i, start_j, visited):
        if word[len(word_so_far) - 1] != word_so_far[-1]:
            return False
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
            # We can use "visited | set([(start_i, start_j)])" to replace the new_visited argument, but it is not necessary and increases time.
            if self.is_word_exist(board, word, word_so_far + board[pos[0]][pos[1]], pos[0], pos[1], new_visited):
                return True
        return False
    
    
# Solution from jiuzhang.com. Conceptually it is similar to my solutions above, but this solution takes longer time to execute.    
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        if board is None or len(board) == 0:
            return []
        
        # pre-process
        # 预处理
        word_set = set(words)
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])
        
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(
                    board,
                    i,
                    j,
                    board[i][j],
                    word_set,
                    prefix_set,
                    set([(i, j)]),
                    result,
                )
                
        return list(result)
        
    def search(self, board, x, y, word, word_set, prefix_set, visited, result):
        if word not in prefix_set:
            return
        
        if word in word_set:
            result.add(word)
        
        for delta_x, delta_y in DIRECTIONS:
            x_ = x + delta_x
            y_ = y + delta_y
            
            if not self.inside(board, x_, y_):
                continue
            if (x_, y_) in visited:
                continue
            
            visited.add((x_, y_))
            self.search(
                board,
                x_,
                y_,
                word + board[x_][y_],
                word_set,
                prefix_set,
                visited,
                result,
            )
            visited.remove((x_, y_))
            
    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
    
# Solution from jiuzhang.com. It uses trie. Each trie node contains some children and an indication of whether 
# it corresponds to the last letter of a word.
DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.word = None
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            child = node.children.get(c)
            if not child:
                node.children[c] = TrieNode()
                child = node.children[c]
            node = child
        node.word = word
        node.is_word = True
    
    # This function is actually not used, but added here for completeness of Trie functions.
    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if not node:
                return None
        return node

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        results = set()
        trie = Trie()
        for word in words:
            trie.add(word)
        
        # We cannot formulate it in the same way as the 2 solutions I came up with.
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(board, i, j, trie.root.children.get(c), results, set())
        return list(results)    
    
    def search(self, board, x, y, node, results, visited):
        if not node:
            return
        if node.is_word:
            results.add(node.word)
            # Don't just return here, because the current node could have descendants.

        new_visited = set(visited)
        new_visited.add((x, y))
        for delta_x, delta_y in DIRECTIONS:
            x_, y_ = x + delta_x, y + delta_y
            if not (0 <= x_ < len(board) and 0 <= y_ < len(board[0])):
                continue
            if (x_, y_) in new_visited:
                continue            
            self.search(board, x_, y_, node.children.get(board[x_][y_]), results, new_visited)

