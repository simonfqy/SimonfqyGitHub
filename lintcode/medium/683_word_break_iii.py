'''
Link: https://www.lintcode.com/problem/683
'''


# My own solution. Uses memoized search. Has O(n^2) time complexity, where n is the length of s.
class Solution:
    """
    @param s: A string
    @param dictionary: A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dictionary):
        self.dictionary = {word.lower() for word in dictionary}
        self.s = s.lower()
        self.inds_to_sentence_count = dict()
        return self.get_num_sentences(0, len(s) - 1)
    
    # End is inclusive.
    def get_num_sentences(self, start, end):
        if (start, end) in self.inds_to_sentence_count:
            return self.inds_to_sentence_count[(start, end)]
        self.inds_to_sentence_count[(start, end)] = 0
        if self.s[start : end + 1] in self.dictionary:
            self.inds_to_sentence_count[(start, end)] += 1
        for i in range(start, end):
            if self.s[start : (i + 1)] not in self.dictionary:
                continue
            self.inds_to_sentence_count[(start, end)] += self.get_num_sentences(i + 1, end)
        return self.inds_to_sentence_count[(start, end)]
        
        
