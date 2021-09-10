'''
Link: https://www.lintcode.com/problem/582/
'''

# My own solution. Using dynamic programming and memorized DFS.
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        n = len(s)
        # Represents whether the s[i: j + 1] is a valid word in wordDict.
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                if s[i : j + 1] in wordDict:
                    dp[i][j] = True
        self.all_valid_words = dict()
        return self.get_all_valid_words(s, 0, n - 1, dp)

    # Return a list of valid words.
    def get_all_valid_words(self, s, i, j, dp):
        if (i, j) in self.all_valid_words:
            return self.all_valid_words[(i, j)]
        new_sentences = []
        for end in range(i, j + 1):
            if dp[i][end]:                
                if end == j:
                    # s[i : end + 1] should be the last matching section of s to the dictionary and it matches to the end.
                    new_sentences.append(s[i : end + 1])
                else:
                    # end is still smaller than j, so push further and see whether there are truly matches.
                    continuing_sentences = self.get_all_valid_words(s, end + 1, j, dp)
                    for continue_sentence in continuing_sentences:
                        # If continuing_sentences is empty, new_sentences is unmodified.
                        new_sentences.append(s[i : end + 1] + " " + continue_sentence)
        self.all_valid_words[(i, j)] = new_sentences
        return new_sentences
    
    
# My own solution, slightly modified from the previous one. Still uses memorized DFS, and the 
# dynamic programming table is removed.
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        n = len(s)
        # Represents whether the s[i: j + 1] is a valid word in wordDict.        
        self.all_valid_words = dict()
        return self.get_all_valid_words(s, 0, n - 1, wordDict)

    # Return a list of valid words.
    def get_all_valid_words(self, s, i, j, wordDict):
        if (i, j) in self.all_valid_words:
            return self.all_valid_words[(i, j)]
        new_sentences = []
        for end in range(i, j + 1):
            substring = s[i : end + 1]
            if substring in wordDict:                
                if end == j:
                    new_sentences.append(substring)
                else:
                    continuing_sentences = self.get_all_valid_words(s, end + 1, j, wordDict)
                    for continue_sentence in continuing_sentences:
                        new_sentences.append(substring + " " + continue_sentence)
        self.all_valid_words[(i, j)] = new_sentences
        return new_sentences
