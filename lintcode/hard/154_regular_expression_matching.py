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
      
