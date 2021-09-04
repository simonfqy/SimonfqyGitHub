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
      
