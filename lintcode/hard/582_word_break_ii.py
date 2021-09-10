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
        if i > j:
            return []
        if (i, j) in self.all_valid_words:
            return self.all_valid_words[(i, j)]
        new_sentences = []
        found_matches = False
        for end in range(i, j + 1):
            if dp[i][end]:
                continuing_sentences = self.get_all_valid_words(s, end + 1, j, dp)
                if end == j:
                    found_matches = True
                    new_sentences.append(s[i : end + 1])
                elif len(continuing_sentences) > 0:
                    found_matches = True
                    for continue_sentence in continuing_sentences:
                        new_sentences.append(s[i : end + 1] + " " + continue_sentence)
        self.all_valid_words[(i, j)] = new_sentences
        return new_sentences
