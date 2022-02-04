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
        
        
# My own solution. Uses dynamic programming. Has O(n^2) time complexity, where n is the length of s.
class Solution:
    """
    @param s: A string
    @param dictionary: A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dictionary):
        self.dictionary = {word.lower() for word in dictionary}
        self.s = s.lower()
        n = len(s)
        # dp[i] represents the number of sentences that can be constructed from s[i : n]. 
        self.dp = [0] * n
        for start in range(n - 1, -1, -1):
            if self.s[start : n] in self.dictionary:
                self.dp[start] += 1
            for second_word_start in range(start + 1, n):
                if self.s[start : second_word_start] not in self.dictionary:
                    continue
                self.dp[start] += self.dp[second_word_start]
        return self.dp[0] 
    
    
# Solution borrowed from jiuzhang.com with my own modifications. It also uses DP, largely similar to the solution above.
# This solution has 1 more entry in the dp array and goes from left to right.
class Solution:
    """
    @param s: A string
    @param dictionary: A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dictionary):
        self.dictionary = {word.lower() for word in dictionary}
        self.s = s.lower()
        n = len(s)
        # dp[i] represents the number of sentences that can be formed by s[0 : i].
        self.dp = [0] * (n + 1)
        # There is 1 way to split empty string.
        self.dp[0] = 1
        for start in range(n):
            for end in range(start, n):
                if self.s[start : end + 1] not in self.dictionary:
                    continue
                self.dp[end + 1] += self.dp[start]
        return self.dp[n] 
    
    
    
