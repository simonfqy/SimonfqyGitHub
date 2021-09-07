# Link: https://www.lintcode.com/problem/192/

# My own solution. Using a 2-d array to store the results for future use. Otherwise,
# it will hit the time exceed limit error. 
class Solution:    
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here
        converted_p = ""
        prev_char = None
        for character in p:
            if character == "*" and prev_char == "*":
                continue
            converted_p += character
            prev_char = character
        self.s_p_matching = [[None]*len(converted_p) for _ in range(len(s))]
        return self.is_match(s, converted_p, 0, 0)

    def is_match(self, s, p, i, j):
        if p and p[j:] == "*":
            for k in range(i, len(s)):
                self.s_p_matching[k][j] = True
            return True
        if i >= len(s) and j >= len(p):
            return True
        if (i >= len(s) and j < len(p)) or (j >= len(p) and i < len(s)):
            return False
        # Both s[i:] and p[j:] are non-empty.
        if self.s_p_matching[i][j] is not None:
            return self.s_p_matching[i][j]
        if p[j].isalpha():
            if p[j] != s[i]:
                self.s_p_matching[i][j] = False
                return False
            result = self.is_match(s, p, i + 1, j + 1)
            self.s_p_matching[i][j] = result
            return result
        if p[j] == '?':
            result = self.is_match(s, p, i + 1, j + 1)
            self.s_p_matching[i][j] = result
            return result
        # Now p[j] is '*'
        for k in range(i, len(s)):            
            if self.is_match(s, p, k, j + 1):
                self.s_p_matching[i][j] = True
                return True
        self.s_p_matching[i][j] = False
        return False
    
      
# Simplified implementation of the version above based on the solution from jiuzhang.com.
class Solution:
    
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here        
        self.s_p_matching = [[None]*len(p) for _ in range(len(s))]
        return self.is_match(s, p, 0, 0)

    def is_match(self, s, p, i, j):        
        if len(s) == i:
            for k in range(j, len(p)):
                if p[k] != "*":
                    return False
            return True
        if len(p) == j:
            return False
        if self.s_p_matching[i][j] is not None:
            return self.s_p_matching[i][j]
        # Now p[j] is not null
        matches = False
        if p[j] == "*":
            matches = self.is_match(s, p, i, j + 1) or self.is_match(s, p, i + 1, j)
        else:
            matches = (p[j] == s[i] or p[j] == "?") and self.is_match(s, p, i + 1, j + 1)         
        self.s_p_matching[i][j] = matches
        return matches
    
        
# Solution from jiuzhang.com. Uses dynamic programming (iteratively) recording the matching of first
# i and j characters of s and p respectively.
# This logic is not very straightforward. It can be incorrect in a number of places if we configure wrongly.
# One notable place is initializing dp with False values: we can't set it to None.
class Solution:
    
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here        
        if not s and not p:
            return False
        m, n = len(s), len(p)
        # Each element dp[i][j] records whether the s[:i] and p[:j] match, i.e., whether
        # the first i characters in s and first j characters in p match.
        # We have to initialize it to False. If to None, it will be incorrect.
        dp = [[False] * (n + 1) for _ in range(m + 1)]        
        dp[0][0] = True
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and p[j - 1] == "*"
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = (s[i - 1] == p[j - 1] or p[j - 1] == "?") and dp[i - 1][j - 1] 

        return dp[m][n]
    
    
# Also a dynamic programming solution from jiuzhang.com. Slightly optimizes the previous solution
# by only having O(n) time complexity, where n is the length of p. It uses the property that each
# i index of s only depends on i-1, so for s we only need 2.
class Solution:
    
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here        
        if not s and not p:
            return False
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(2)]
        dp[0][0] = True
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and p[j - 1] == "*"
        for i in range(1, m + 1):
            # We have to add this line to avoid errors. It is not present with the O(n*m) DP solution.
            dp[i % 2][0] = False
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i % 2][j] = dp[(i - 1) % 2][j] or dp[i % 2][j - 1]
                else:
                    dp[i % 2][j] = (p[j - 1] == "?" or p[j - 1] == s[i - 1]) and dp[(i - 1)%2][j - 1]
        return dp[m % 2][n]
