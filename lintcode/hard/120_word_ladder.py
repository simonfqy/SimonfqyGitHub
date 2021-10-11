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
