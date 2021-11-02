'''
https://www.lintcode.com/problem/1726
'''

# My own solution. Originally hits time limit exceeded exception without removing duplicate b words. After the duplication
# removal, the performance is pretty well. Assuming A has size n and B has size m, and words in A and B have max length k, then
# the time complexity is O(mnk^2).
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
        visited_b = set()
        for b_word in B:
            # Before having this duplicate removal of b_words, it hit time limit exceeded exception.
            sorted_b_word = ''.join(sorted(b_word))
            if sorted_b_word in visited_b:
                continue
            subset = self.get_subset(subset, a_word_to_sorted_word, sorted_b_word, visited_b)     
            visited_b.add(sorted_b_word)       
        return subset
    
    def get_subset(self, subset, a_word_to_sorted_word, sorted_b_word, visited_b):
        new_subset = []
        for a_word in subset:
            sorted_a_word = a_word_to_sorted_word[a_word]
            if self.b_word_in_a_word(sorted_a_word, sorted_b_word):
                new_subset.append(a_word)
        return new_subset

    def b_word_in_a_word(self, sorted_a_word, sorted_b_word):
        prev = 0
        for i in range(len(sorted_b_word)):
            char = sorted_b_word[i]
            if char == sorted_b_word[prev]:
                # There are actually two scenarios, one in which i == len(sorted_b_word) - 1, one with i smaller than that.
                # But both will be okay with this "continue" statement.
                continue
            if sorted_b_word[prev : i] not in sorted_a_word:
                return False
            prev = i
        return sorted_b_word[prev:] in sorted_a_word            
            
