'''
Link: https://www.lintcode.com/problem/780/
'''

# My own solution. It is very slow, we need to use memoization to improve its performance. When we use prefixes in the recursive
# function parameters, we CANNOT use memoization, otherwise we'll have errors!
class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        return self.get_longest_valid_strings(s, 0, "", 0)

    def get_longest_valid_strings(self, s, start, prefix, left_minus_right_count):
        if start >= len(s):
            if left_minus_right_count == 0:
                return [prefix]
            return [""]
        # NOTE: if we have prefix, we shouldn't use memoization, otherwise we'll have wrong answers. Remember it!
        # if start in self.memo:
        #     return self.memo[start]
        valid_strings = set()
        if s[start] == "(":
            valid_strings.update(self.get_longest_valid_strings(s, start + 1, prefix + s[start], left_minus_right_count + 1))
            valid_strings.update(self.get_longest_valid_strings(s, start + 1, prefix, left_minus_right_count))
        elif s[start] == ")":
            valid_strings.update(self.get_longest_valid_strings(s, start + 1, prefix, left_minus_right_count))
            if left_minus_right_count > 0:
                valid_strings.update(self.get_longest_valid_strings(s, start + 1, prefix + s[start], left_minus_right_count - 1))
        else:
            valid_strings.update(self.get_longest_valid_strings(s, start + 1, prefix + s[start], left_minus_right_count))
        if not valid_strings:            
            return [""]
        max_length = max([len(string) for string in valid_strings])
        longest_valid_strings = [string for string in valid_strings if len(string) == max_length]
        
        # self.memo[start] = longest_valid_strings
        return longest_valid_strings
    
    
# This solution doesn't work. Putting here to serve as a reminder, recording negative findings too.
class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        return self.helper(s, 0, "", 0)

    def helper(self, s, start, prefix, left_minus_right_count):
        if start >= len(s):
            if left_minus_right_count == 0:
                return [prefix]
            return [""]
        valid_strings = set()
        for i in range(start, len(s)):
            if s[i] == "(":
                valid_strings.update(self.helper(s, i + 1, prefix + s[i], left_minus_right_count + 1))
            elif s[i] == ")":
                if left_minus_right_count == 0:                    
                    continue
                valid_strings.update(self.helper(s, i + 1, prefix + s[i], left_minus_right_count - 1))
            else:
                valid_strings.update(self.helper(s, i + 1, prefix + s[i], left_minus_right_count))
                
        max_len = max([len(string) for string in valid_strings])
        return [string for string in valid_strings if len(string) == max_len]
