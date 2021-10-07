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
    
    
# My own solution, using BFS without queue, should be correct, but causes memory limit exceeded exception.
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dictionary):
        min_length_found = False
        temp = [[start]]
        self.word_dist = dict()
        visited_words = set([start])
        results = []
        while not min_length_found:
            buff = []
            newly_visited = set()
            # Every time the execution enters this for loop, the length of the (under-construction) word ladder
            # is the same. So all lists in temp have the same length.
            for i in range(len(temp)):
                curr_word = temp[i][-1]
                if self.calc_word_dist(curr_word, end) == 1:
                    results.append(temp[i] + [end])
                    min_length_found = True
                if min_length_found:
                    continue
                for word in dictionary:
                    # If the current word is visited by some other branches earlier (when the word ladder is shorter),
                    # there's no point in diving into it any further; the current branch is guaranteed to be non-optimal.
                    if word in visited_words:
                        continue
                    if self.calc_word_dist(curr_word, word) == 1:
                        buff.append(temp[i] + [word])
                        newly_visited.add(word)
            visited_words.update(newly_visited)
            temp = buff
        return results
    
    def calc_word_dist(self, from_word, to_word):
        if (from_word, to_word) in self.word_dist:
            return self.word_dist[(from_word, to_word)]
        if (to_word, from_word) in self.word_dist:
            return self.word_dist[(to_word, from_word)]
        distance = 0
        for i in range(len(from_word)):
            if from_word[i] != to_word[i]:
                distance += 1                
        self.word_dist[(from_word, to_word)] = distance
        return distance
