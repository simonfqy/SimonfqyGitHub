'''
Link: https://www.lintcode.com/problem/154/
See https://github.com/simonfqy/SimonfqyGitHub/blob/master/lintcode/hard/192_wildcard_matching.py, that question is very similar to this one.
'''

# My own solution using memorized DFS, recursive.
class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        self.memo = [[None]*len(p) for _ in range(len(s))]
        return self.is_match(s, p, 0, 0)

    def is_match(self, s, p, i, j):
        if j >= len(p):
            return i >= len(s)
        if i >= len(s):
            return j >= len(p) - 2 and p[-1] == "*"
        if self.memo[i][j] is not None:
            return self.memo[i][j]
        matches = False
        if p[j] == "*":
            if self.is_match(s, p, i, j + 1):
                matches = True
            elif self.is_match(s, p, i + 1, j):
                matches = p[j - 1] == "." or p[j - 1] == s[i]
        else:
            matches = ((p[j] == "." or p[j] == s[i]) and self.is_match(s, p, i + 1, j + 1)) or \
                (j < len(p) - 1 and p[j + 1] == "*" and self.is_match(s, p, i, j + 2))

        self.memo[i][j] = matches
        return matches
    
    
# The solution from jiuzhang.com, I only slightly modified it. Also uses memorized DFS. The basic idea is similar to my solution above.
class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        self.memo = [[None]*len(p) for _ in range(len(s))]
        return self.is_match(s, p, 0, 0)

    def is_match(self, s, p, i, j):
        if j >= len(p):
            return i >= len(s)
        if i >= len(s):            
            return self.can_p_be_empty(p, j)
        if self.memo[i][j] is not None:
            return self.memo[i][j]
        matches = False
        if j <= len(p) - 2 and p[j + 1] == "*":
            matches = self.is_match(s, p, i, j + 2) or (self.char_matches(s[i], p[j]) and self.is_match(s, p, i + 1, j))
        else:
            # p[j] cannot be "*", because that case will be handled by the if-body when j is j-1.
            # The only cases here should be j == len(p) - 1, or p[j] not being "*" and neither is p[j + 1].
            # In either case, we need to match s[i] with p[j]
            matches = self.char_matches(s[i], p[j]) and self.is_match(s, p, i + 1, j + 1)

        self.memo[i][j] = matches
        return matches

    def char_matches(self, s, p):
        return p == "." or p == s
    
    # Due us always checking for p[j + 1] == "*", and the guarantee that consecutive "*" never appear, 
    # p[j:] will always start with non "*" characters. Hence we can use this function. If it is using my own
    # implementation, we cannot do it similarly.
    def can_p_be_empty(self, p, j):
        for ind in range(j, len(p), 2):
            if ind >= len(p) - 1 or p[ind + 1] != "*":
                return False
        return True
    
      
# My own solution, iterative DP.
class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        m, n = len(s), len(p)
        # dp[i][j] shows the matching status between s[:i] and p[:j], which is the first i characters of s and first j characters of p.
        dp = [[False]*(n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == "*" and dp[0][j - 2]:
                dp[0][j] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    # dp[i][j - 2] corresponds to the situation where "*" corresponds to 0 occurrence, while the body after "or" corresponds to
                    # "*" matching 1 or more occurrences of the pattern before it.
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (p[j - 2] == "." or p[j - 2] == s[i - 1]))
                else:
                    # p[j - 1] is "." or alphabet.
                    dp[i][j] = dp[i - 1][j - 1] and (p[j - 1] == "." or s[i - 1] == p[j - 1])                    

        return dp[m][n]
    
    
# A variant of the solution above. This time it only has O(n) space complexity, where n is the length of p.
# It uses the property that for each dp[i][j], among all previous rows, it only depends on the immediate row above: i - 1. 
class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        m, n = len(s), len(p)
        dp = [[False]*(n + 1) for _ in range(2)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == "*" and dp[0][j - 2]:
                dp[0][j] = True

        for i in range(1, m + 1):
            dp[i % 2][0] = False
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i % 2][j] = dp[i % 2][j - 2] or (dp[(i - 1) % 2][j] and (p[j - 2] == "." or p[j - 2] == s[i - 1]))
                else:
                    # p[j - 1] is "." or alphabet.
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1] and (p[j - 1] == "." or s[i - 1] == p[j - 1])                    

        return dp[m % 2][n]    
