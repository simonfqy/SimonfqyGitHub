'''
https://www.lintcode.com/problem/171/
'''

# My own solution. Uses the built-in sorting function to get the sorted words.
class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        results = []
        sorted_word_to_original_words = dict()
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in sorted_word_to_original_words:
                sorted_word_to_original_words[sorted_word] = []
            sorted_word_to_original_words[sorted_word].append(word)
        
        for sorted_word in sorted_word_to_original_words:
            if len(sorted_word_to_original_words[sorted_word]) > 1:
                results.extend(sorted_word_to_original_words[sorted_word])
        return results
    
    
# My own solution. Slightly modified based on the solution above. Constructs the return list while traversing through the
# strs, does not need to visit the words twice.
class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        results = []
        sorted_word_to_original_words = dict()
        sorted_word_visited = set()
        for word in strs:
            sorted_word = ''.join(sorted(list(word)))
            if sorted_word not in sorted_word_to_original_words:
                sorted_word_to_original_words[sorted_word] = [word]
            else:
                if sorted_word not in sorted_word_visited:
                    results += sorted_word_to_original_words[sorted_word]
                    sorted_word_visited.add(sorted_word)
                results.append(word)

        return results
