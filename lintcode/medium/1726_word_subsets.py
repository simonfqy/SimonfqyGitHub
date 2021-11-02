'''
https://www.lintcode.com/problem/1726
'''

# My own solution. Should be correct, but hits time limit exceeded exception.
class Solution:
    """
    @param A: a string array
    @param B: a string array
    @return: return an string array 
    """
    def wordSubsets(self, A, B):
        subset = A
        a_word_to_sorted_word = dict()
        for a_word in A:
            a_word_to_sorted_word[a_word] = ''.join(sorted(a_word))
        for b_word in B:
            subset = self.get_subset(subset, a_word_to_sorted_word, b_word)
            if not subset:
                return []
        return subset
    
    def get_subset(self, subset, a_word_to_sorted_word, b_word):
        new_subset = []
        for a_word in subset:
            sorted_a_word = a_word_to_sorted_word[a_word]
            sorted_b_word = ''.join(sorted(b_word))
            if self.b_word_in_a_word(sorted_a_word, sorted_b_word):
                new_subset.append(a_word)
        return new_subset

    def b_word_in_a_word(self, sorted_a_word, sorted_b_word):
        prev = 0
        for i in range(len(sorted_b_word)):
            char = sorted_b_word[i]
            if char == sorted_b_word[prev]:
                if i < len(sorted_b_word) - 1:
                    continue
                else:
                    return sorted_b_word[prev:] in sorted_a_word
            if sorted_b_word[prev : i] not in sorted_a_word:
                return False
            prev = i
        return sorted_b_word[prev:] in sorted_a_word
            
