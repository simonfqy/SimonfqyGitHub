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

    # Return a list of valid sentences that we can obtain from s[i : j + 1].
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
        self.all_valid_words = dict()
        return self.get_all_valid_words(s, 0, n - 1, wordDict)

    # Return a list of valid sentences that we can obtain from s[i : j + 1].
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
    
    
# This solution is translated from the Java solution in Jiuzhang.com. It uses memorized DFS.
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):        
        # write your code here
        self.sentences = []
        # The self.starting_substring_is_sentence[i] indicates whether the substring s[i:] can be divided into a valid sentence. 
        # We have to initialize it to True, otherwise the self.dfs() will exit during the first iteration.
        self.starting_substring_is_sentence = [True] * len(s)
        self.dfs(0, s, wordDict, "")
        return self.sentences
        
    def dfs(self, start_ind, s, wordDict, sentence_so_far):
        if start_ind == len(s):
            self.sentences.append(sentence_so_far)
            return True
        if not self.starting_substring_is_sentence[start_ind]:
            return False
        if start_ind > 0:
            sentence_so_far += " "
        found_match_for_current_substring_start_ind = False
        current_word = ""
        for i in range(start_ind, len(s)):
            current_word += s[i]
            if current_word in wordDict:
                # Starts the search of the next level based on the sentence constructed so far.
                found_match_for_current_substring_start_ind |= self.dfs(i + 1, s, wordDict, sentence_so_far + current_word)

        self.starting_substring_is_sentence[start_ind] = found_match_for_current_substring_start_ind
        return found_match_for_current_substring_start_ind
    
    
# Slightly modified from the previous solution, here the self.dfs() function no longer returns boolean.
# It is less intuitive, but it still works correctly.
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):        
        # write your code here
        self.sentences = []
        # Have to initialize to True, otherwise the self.dfs() will exit during the first iteration.
        self.starting_substring_is_sentence = [True] * len(s)
        self.dfs(0, s, wordDict, "")
        return self.sentences
        
    def dfs(self, start_ind, s, wordDict, sentence_so_far):
        if start_ind == len(s):
            self.sentences.append(sentence_so_far)
            return
        if not self.starting_substring_is_sentence[start_ind]:
            return
        if start_ind > 0:
            sentence_so_far += " "
        current_word = ""
        found_match_for_current_substring_start_ind = False
        for i in range(start_ind, len(s)):
            current_word += s[i]
            if current_word in wordDict:
                self.dfs(i + 1, s, wordDict, sentence_so_far + current_word)
                if (i == len(s) - 1 or self.starting_substring_is_sentence[i + 1]):
                    found_match_for_current_substring_start_ind = True 

        self.starting_substring_is_sentence[start_ind] = found_match_for_current_substring_start_ind
        
        
# Solution from jiuzhang.com using dynamic programming and DFS. I translated it to Python.
# In concept it is pretty similar to the solution above. The difference is that, this solution uses dynamic programming
# to decide the cutting points, which is done in the wordBreak() function itself, while the solution above uses self.dfs()
# function for this determination, making that function much heavier weight.
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):        
        # write your code here
        self.possible_sentences = []
        n = len(s)
        self.valid_cutting_points_for_each_start_ind = [[] for _ in range(n)]
        # Start from the end of the string to make sure that the 2d array valid_cutting_points_for_each_start_ind
        # is properly constructed. It first checks whether the s[n - 1] is part of a word in the wordDict.
        for i in range(n - 1, -1, -1):
            for j in range(i, n + 1):
                substring = s[i : j]
                if substring not in wordDict:
                    continue
                # j is the index of either the element after the end of the string, or the starting element of 
                # the next word in a sentence that eventually leads to the end of the string.
                if j == n or self.valid_cutting_points_for_each_start_ind[j]:
                    self.valid_cutting_points_for_each_start_ind[i].append(j)
        self.dfs(0, s, "")
        return self.possible_sentences
    
    # The dfs() function is really light-weight in this solution.
    def dfs(self, start_ind, s, sentence_so_far):
        if start_ind == len(s):
            self.possible_sentences.append(sentence_so_far)
            return
        if start_ind > 0:
            sentence_so_far += " "
        for p in self.valid_cutting_points_for_each_start_ind[start_ind]:
            self.dfs(p, s, sentence_so_far + s[start_ind : p])
            
            
# This solution should be correct, but doesn't work due to time limit exceeded. I was trying to
# construct a classical DP algorithm here and let later DP cells be calculated based on prior DP cells.
# It is more complicated than desirable.
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):        
        # write your code here
        n = len(s)       
        # all_valid_sentences[(i, j)] is the list of all sentences that can be broken from s[i : j + 1] 
        all_valid_sentences = dict()
        self.already_accumulated = dict()
        # I was trying to construct the DP table in one go.
        for end in range(n):
            for start in range(end, -1, -1):
                # start and end indices are inclusive.
                if (start, end) not in all_valid_sentences:
                    all_valid_sentences[(start, end)] = []
                substring = s[start : end + 1]
                if substring in wordDict:                    
                    all_valid_sentences[(start, end)].append(substring)
                all_valid_sentences[(start, end)] = self.get_accumulated_sentences(all_valid_sentences, start, end)               

        return all_valid_sentences[(0, n - 1)] 

    # Gets all the valid sentences (including single word) that can be constructed from s[start: end + 1]
    def get_accumulated_sentences(self, all_valid_sentences, start, end):
        accumulated_sentences = []
        # Even if we have a set with the same content as accumulated_sentences, it still times out.
        if (start, end) in self.already_accumulated:
            return all_valid_sentences[(start, end)]
        for mid in range(start, end + 1):
            if not all_valid_sentences[(start, mid)]:
                continue
            intermediate_sentences = all_valid_sentences[(start, mid)]
            if mid == end:
                accumulated_sentences.extend(intermediate_sentences)        
            else:
                continuing_sentences = self.get_accumulated_sentences(all_valid_sentences, mid + 1, end)
                for interm_sentence in intermediate_sentences:
                    for cont_sentence in continuing_sentences:
                        composed_sentence = interm_sentence + " " + cont_sentence
                        if composed_sentence in accumulated_sentences:
                            continue
                        accumulated_sentences.append(composed_sentence)
        self.already_accumulated[(start, end)] = True
        return accumulated_sentences
