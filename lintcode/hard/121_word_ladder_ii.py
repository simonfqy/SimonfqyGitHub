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
        word_to_earliest_ind = dict()
        word_to_earliest_ind[start] = 0
        self.helper(start, end, [start], dictionary, word_to_earliest_ind)
        return self.lists

    def helper(self, curr_word, end, path_so_far, dictionary, word_to_earliest_ind):
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
            if end in word_to_earliest_ind and word_to_earliest_ind[end] < len(path_so_far):
                return
            word_to_earliest_ind[end] = len(path_so_far)
            self.helper(end, end, path_so_far + [end], dictionary, word_to_earliest_ind)
            return
        for word in dictionary:
            if word in path_so_far:
                continue
            if word in word_to_earliest_ind and word_to_earliest_ind[word] < len(path_so_far):
                continue
            if self.letter_distance(curr_word, word) == 1:
                word_to_earliest_ind[word] = len(path_so_far)
                self.helper(word, end, path_so_far + [word], dictionary, word_to_earliest_ind)
    
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

# My own solution. Should be correct, but still hits time limit exceeded exception (though there is significant improvement compared to 
# solution 1 which uses unidirectional DFS). Uses bidirectional DFS to start from both start and end.
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dictionary):
        self.distance_one = dict()
        self.word_to_dist_to_start = dict()
        self.word_to_dist_to_start[start] = 0
        self.word_to_dist_to_end = dict()
        self.word_to_dist_to_end[end] = 0
        return self.helper(start, end, dictionary, set(), set(), len(dictionary | {start} | {end}))

    # Returns the shortest lists of words leading from start to end.
    def helper(self, start, end, dictionary, words_before_start, words_after_end, max_possible_length):
        if max_possible_length <= 0:
            return [None]
        if start == end:
            return [[start]]
        if max_possible_length <= 1:
            return [None]
        if self.is_distance_one(start, end):
            return [[start, end]]
        if max_possible_length <= 2:
            return [None]
        next_start_words = []
        next_end_words = []
        for word in dictionary:
            if word in words_before_start or word in words_after_end:
                continue
            if word == start or word == end:
                continue
            if self.is_distance_one(start, word):
                if word in self.word_to_dist_to_start and self.word_to_dist_to_start[word] < len(words_before_start) + 1:
                    continue
                next_start_words.append(word)
                self.word_to_dist_to_start[word] = len(words_before_start) + 1
            if self.is_distance_one(word, end):
                if word in self.word_to_dist_to_end and self.word_to_dist_to_end[word] < len(words_after_end) + 1:
                    continue
                next_end_words.append(word)
                self.word_to_dist_to_end[word] = len(words_after_end) + 1
        
        new_words_before_start = words_before_start | {start}
        new_words_after_end = words_after_end | {end}        
        possible_length = max_possible_length - 2
        shortest_candidates = []
        for new_start in next_start_words:
            for new_end in next_end_words:
                shorter_candidates = self.helper(new_start, new_end, dictionary, new_words_before_start, new_words_after_end, possible_length)
                for candidate in shorter_candidates:
                    if candidate is None:
                        continue
                    if len(candidate) < possible_length:
                        possible_length = len(candidate)
                        shortest_candidates = []
                    shortest_candidates.append(candidate)
        results = []
        for cand in shortest_candidates:
            results.append([start] + cand + [end])
        return results                                      

    def is_distance_one(self, from_word, to_word):
        if (from_word, to_word) in self.distance_one:
            return self.distance_one[(from_word, to_word)]
        if (to_word, from_word) in self.distance_one:
            return self.distance_one[(to_word, from_word)]
        distance = 0
        for i in range(len(from_word)):
            if from_word[i] != to_word[i]:
                distance += 1
                if distance > 1:
                    break
        self.distance_one[(from_word, to_word)] = distance == 1
        return distance == 1
           
