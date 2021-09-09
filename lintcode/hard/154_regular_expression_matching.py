'''
Link: https://www.lintcode.com/problem/154/
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
    
      
# My own solution iterative DP.
class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        m, n = len(s), len(p)
        dp = [[False]*(n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == "*" and dp[0][j - 2]:
                dp[0][j] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or (dp[i - 1][j] and (p[j - 2] == "." or p[j - 2] == s[i - 1]))
                else:
                    # p[j - 1] is "." or alphabet.
                    dp[i][j] = dp[i - 1][j - 1] and (p[j - 1] == "." or s[i - 1] == p[j - 1])                    

        return dp[m][n]
