'''
Link: https://www.lintcode.com/problem/121/
'''

# My own solution, DFS. Should be correct but causes time limit exceeded exception. The time complexity should be O(n!), where
# n is the number of words in the dictionary.
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dictionary):
        # Even manually setting the self.min_length to a small number, say 11 or 12, still hits time limit exceeded exception. 
        self.min_length = len(dictionary | {start} | {end})
        self.lists = []
        self.pair_distance = dict()
        self.helper(start, end, [start], dictionary)
        return self.lists

    def helper(self, curr_word, end, path_so_far, dictionary):
        if len(path_so_far) + self.letter_distance(curr_word, end) > self.min_length:
            return
        if curr_word == end:
            size = len(path_so_far)
            if size < self.min_length:
                self.lists = []
                self.min_length = size
            self.lists.append(path_so_far)            
            return
        if self.letter_distance(curr_word, end) == 1:
            self.helper(end, end, path_so_far + [end], dictionary)
            return
        for word in dictionary:
            if word in set(path_so_far):
                continue
            if self.letter_distance(curr_word, word) == 1:
                self.helper(word, end, path_so_far + [word], dictionary)
    
    def letter_distance(self, from_word, to_word):
        if (from_word, to_word) in self.pair_distance:
            return self.pair_distance[(from_word, to_word)]
        if (to_word, from_word) in self.pair_distance:
            return self.pair_distance[(to_word, from_word)]
        total_distance = 0
        for i in range(len(from_word)):
            if from_word[i] != to_word[i]:
                total_distance += 1                
        self.pair_distance[(from_word, to_word)] = total_distance
        return total_distance
