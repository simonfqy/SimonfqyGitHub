'''
Link: https://www.lintcode.com/problem/word-ladder/description
'''

# This solution is almost copied from Jiuzhang.com. Let m be the length of each word, n be the total number
# of words in the dictionary, the total time complexity is O(nm^2). That is because we need to generate new words
# for O(nm) times, and generating each new word involves substring operation which has a time complexity of O(m),
# so the total time complexity is O(nm^2).
from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    
    def ladderLength(self, start, end, dict):
        # This dict.add(end) is crucial. Otherwise all inputs will get 0 returned.
        dict.add(end)
        length = 0
        visited = set([start])
        queue = deque([start])
        while queue:
            length += 1
            for _ in range(len(queue)):
                this_word = queue.popleft()
                
                if this_word == end:
                    return length
                
                for word in self.get_next_words(this_word):
                    if word not in dict:
                        continue
                    if word in visited:
                        continue
                    queue.append(word)
                    # Be aware of the position of this visited.add(). If it is put after this_word=queue.popleft(),
                    # it will cause runtime exceeded anomaly. It is because in that case, the visited set is not
                    # populated fast enough, many words are unnecessarily visited more than once. So populate the 
                    # visited set early can avoid this problem. Always remember.
                    visited.add(word)                    
        return 0        
        
    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for char in "abcdefghijklmnopqrstuvwxyz":
                if char == word[i]:
                    continue
                words.append(left + char + right)
        return words
    
    
# Solution from jiuzhang.com, it doesn't use level order traversal (层次遍历).     
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict.add(end)
        queue = collections.deque([start])
        distance = {start: 1}
            
        while queue:
            word = queue.popleft()
            if word == end:
                return distance[word]
            
            for next_word in self.get_next_words(word, dict):
                if next_word in distance:
                    continue
                queue.append(next_word)
                distance[next_word] = distance[word] + 1

        return 0
        
    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                next_word = left + char + right
                if next_word in dict:
                    words.append(next_word)

        return words    
    
# Bidirectional BFS solution from jiuzhang.com.    
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, wordSet):
        if start == end:
            return 1
        
        wordSet.add(start)
        wordSet.add(end)
        graph = self.construct_graph(wordSet)
        
        forward_queue = collections.deque([start])
        forward_set = set([start])
        backward_queue = collections.deque([end])
        backward_set = set([end])

        distance = 1
        while forward_queue and backward_queue:
            distance += 1
            if self.extend_queue(graph, forward_queue, forward_set, backward_set):
                return distance
            distance += 1
            if self.extend_queue(graph, backward_queue, backward_set, forward_set):
                return distance        
        return -1
        
    def extend_queue(self, graph, queue, visited, opposite_visited):
        for _ in range(len(queue)):
            word = queue.popleft()
            for next_word in graph[word]:
                if next_word in visited:
                    continue
                if next_word in opposite_visited:
                    return True
                queue.append(next_word)
                visited.add(next_word)
        return False
    
    # This function is very simple, don't overcomplicate it by using queues. Implementing it with queue is problematic.      
    def construct_graph(self, wordSet):
        graph = {}
        for word in wordSet:
            graph[word] = self.get_next_words(word, wordSet)
        return graph
    
    def get_next_words(self, word, wordSet):
        next_word_set = set()
        for i in range(len(word)):
            prefix = word[:i]
            suffix = word[i + 1:]
            chars = list('abcdefghijklmnopqrstuvwxyz')
            chars.remove(word[i])
            for char in chars:
                next_word = prefix + char + suffix
                if next_word in wordSet:
                    next_word_set.add(next_word)
        return next_word_set
