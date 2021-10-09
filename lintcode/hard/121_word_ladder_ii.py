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

    
# My own solution, using BFS and follows the solution above, but changing the way to store distance info. It actually works, though
# rather slow, it doesn't hit the time limit exceeded exception anymore. We no longer calculate the 1-1 string distance between
# pairs of words in dictionary; instead, we generate the distance = 1 neighbors for each word. This way we reduce the distance calculation 
# time complexity from O(k*n^2) (where k is the length of words, n is the number of words) to O(kn), since the set element identity determination is O(1).
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dictionary):
        if start == end:
            return [[start]]
        self.word_to_distance_one_neighbors = dict()
        self.words_whose_distance_analyzed = set()
        dictionary.update({start, end})
        temp = [[start]]
        shortest_sequence_found = False
        results = []
        visited_words = set([start])
        while not shortest_sequence_found:
            buff = []
            newly_visited = set()
            for i in range(len(temp)):
                last_word = temp[i][-1]           
                self.populate_distance_dicts(last_word, dictionary)
                for neighbor in self.word_to_distance_one_neighbors[last_word]:
                    if neighbor in visited_words:
                        continue
                    # A slight modification from the solution above: once a neighbor is the desired end, we won't be
                    # adding other neighbors to the list. This can save some time, because the number of elements at the
                    # bottom of the search tree is large.
                    if neighbor == end:
                        shortest_sequence_found = True
                        results.append(temp[i] + [neighbor])
                        continue
                    if shortest_sequence_found:
                        continue
                    newly_visited.add(neighbor)
                    buff.append(temp[i] + [neighbor])
            visited_words.update(newly_visited)
            temp = buff
        return results

    def populate_distance_dicts(self, from_word, dictionary):
        if from_word in self.words_whose_distance_analyzed:
            return
        if from_word not in self.word_to_distance_one_neighbors:
            self.word_to_distance_one_neighbors[from_word] = set()
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        results = []
        for i, char in enumerate(from_word):
            for new_char in alphabets:
                if new_char == char:
                    continue
                new_word = from_word[:i] + new_char + from_word[i + 1:]
                if new_word not in dictionary:
                    continue
                if new_word in self.word_to_distance_one_neighbors[from_word]:
                    continue
                results.append(new_word)
                self.word_to_distance_one_neighbors[from_word].add(new_word)
                if new_word not in self.word_to_distance_one_neighbors:
                    self.word_to_distance_one_neighbors[new_word] = set()
                self.word_to_distance_one_neighbors[new_word].add(from_word)
        self.words_whose_distance_analyzed.add(from_word)
        return results    
    
    
# My own solution, it uses bidirectional DFS to start from both start and end. Should be correct, but still hits time limit exceeded exception 
# (though there is significant improvement compared to solution 1 which uses unidirectional DFS). 
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
           
# A modification of the version above, also using bidirectional DFS. But this time, we no longer calculate the 1-1 string distance between
# pairs of words in dictionary, we generate the distance = 1 neighbors for each word. This way we reduce the distance calculation time complexity
# from O(k*n^2) (where k is the length of words, n is the number of words) to O(kn), since the set element identity determination is O(1).
# It has some improvements over the solution above, but still hits time limit exceeded exception.
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dictionary):
        self.words_to_distance_one_neighbor = dict()
        self.words_whose_distance_analyzed = set()
        dictionary = set(dictionary)
        self.word_to_dist_to_start = dict()
        self.word_to_dist_to_start[start] = 0
        self.word_to_dist_to_end = dict()
        self.word_to_dist_to_end[end] = 0
        return self.helper(start, end, dictionary, set(), set(), len(dictionary | {start} | {end}))

    # Returns the shortest lists of words leading from start to end.
    def helper(self, start, end, dictionary, words_before_start, words_after_end, max_possible_length):
        if max_possible_length <= 0:
            return []
        if start == end:
            return [[start]]
        if max_possible_length <= 1:
            return []
        if self.is_distance_one(start, end, dictionary):
            return [[start, end]]
        if max_possible_length <= 2:
            return []
        next_start_words = []
        next_end_words = []
        for word in dictionary:
            if word in words_before_start or word in words_after_end:
                continue
            if word == start or word == end:
                continue
            if self.is_distance_one(start, word, dictionary):
                if word in self.word_to_dist_to_start and self.word_to_dist_to_start[word] < len(words_before_start) + 1:
                    continue
                next_start_words.append(word)
                self.word_to_dist_to_start[word] = len(words_before_start) + 1
            if self.is_distance_one(word, end, dictionary):
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

    def is_distance_one(self, from_word, to_word, dictionary):
        if from_word in self.words_to_distance_one_neighbor and to_word in self.words_to_distance_one_neighbor[from_word]:
            return True
        if from_word in self.words_whose_distance_analyzed:
            return False
        if from_word not in self.words_to_distance_one_neighbor:
            self.words_to_distance_one_neighbor[from_word] = set()
        if to_word not in self.words_to_distance_one_neighbor:
            self.words_to_distance_one_neighbor[to_word] = set()
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for i, char in enumerate(from_word):
            for new_char in alphabets:
                if new_char == char:
                    continue
                new_word = from_word[:i] + new_char + from_word[i + 1:]
                if new_word not in dictionary:
                    continue
                if new_word in self.words_to_distance_one_neighbor[from_word]:
                    continue
                self.words_to_distance_one_neighbor[from_word].add(new_word)
                if new_word not in self.words_to_distance_one_neighbor:
                    self.words_to_distance_one_neighbor[new_word] = set()
                self.words_to_distance_one_neighbor[new_word].add(from_word)                    
        self.words_whose_distance_analyzed.add(from_word)        
        return to_word in self.words_to_distance_one_neighbor[from_word]      
    
    
# My own bidirectional BFS solution without using queue. It is a very nasty solution, the repetition makes it bug-prone. But it is
# also the fastest solution I've written so far. 
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dictionary):
        if start == end:
            return [[start]]
        self.words_whose_distances_were_analyzed = set()
        self.words_to_distance_one_neighbors = dict()
        shortest_sequence_found = False
        results = []
        dictionary.update({start, end})
        temp_start, temp_end = [[start]], [[end]]
        visited_from_front, visited_from_rear = set([start]), set([end])
        
        while not shortest_sequence_found:
            buff_start, buff_end = [], []
            newly_visited_start, newly_visited_end = set(), set()
            frontward_search_word_to_ind = dict()
            first_words_in_end_sequences = [sequence[0] for sequence in temp_end]
            
            # This for loop processes the search from start to end.
            for i in range(len(temp_start)):
                start_sequence = temp_start[i]
                curr_word = start_sequence[-1]
                # Catches matches here.
                for j, end_sequence_starting_word in enumerate(first_words_in_end_sequences):
                    if curr_word != end_sequence_starting_word:
                        continue
                    shortest_sequence_found = True
                    results.append(start_sequence + temp_end[j][1:])
                if shortest_sequence_found:
                    continue                
                self.populate_distance_dict(curr_word, dictionary)
                for neighbor in self.words_to_distance_one_neighbors[curr_word]:
                    if neighbor in visited_from_front:
                        continue
                    buff_start.append(start_sequence + [neighbor])
                    newly_visited_start.add(neighbor)
                    if neighbor not in frontward_search_word_to_ind:
                        frontward_search_word_to_ind[neighbor] = set()
                    frontward_search_word_to_ind[neighbor].add(len(buff_start) - 1)                    
            
            temp_start = buff_start
            if shortest_sequence_found:
                break
                
            # This for loop processes the search from end to start.
            for j in range(len(temp_end)):
                end_sequence = temp_end[j]
                curr_end_word = end_sequence[0]
                # Catches potential matches.
                if curr_end_word in frontward_search_word_to_ind:
                    shortest_sequence_found = True
                    for temp_start_ind in frontward_search_word_to_ind[curr_end_word]:
                        results.append(temp_start[temp_start_ind] + end_sequence[1:])
                if shortest_sequence_found:
                    continue
                self.populate_distance_dict(curr_end_word, dictionary)
                for neighbor in self.words_to_distance_one_neighbors[curr_end_word]:
                    if neighbor in visited_from_rear:
                        continue
                    buff_end.append([neighbor] + end_sequence)
                    newly_visited_end.add(neighbor)
            temp_end = buff_end
            visited_from_front.update(newly_visited_start)
            visited_from_rear.update(newly_visited_end)
        return results
    
    def populate_distance_dict(self, from_word, dictionary):
        if from_word in self.words_whose_distances_were_analyzed:
            return
        if from_word not in self.words_to_distance_one_neighbors:
            self.words_to_distance_one_neighbors[from_word] = set()
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for i, char in enumerate(from_word):
            for new_char in alphabets:
                if new_char == char:
                    continue
                new_word = from_word[:i] + new_char + from_word[i + 1:]
                if new_word not in dictionary:
                    continue
                if new_word in self.words_to_distance_one_neighbors[from_word]:
                    continue
                self.words_to_distance_one_neighbors[from_word].add(new_word)
                if new_word not in self.words_to_distance_one_neighbors:
                    self.words_to_distance_one_neighbors[new_word] = set()                
                self.words_to_distance_one_neighbors[new_word].add(from_word)
        self.words_whose_distances_were_analyzed.add(from_word)
