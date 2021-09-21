'''
Link: https://www.lintcode.com/problem/780/
'''

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
        if len(valid_strings) == 0:
            self.memo[start] = [""]
            return [""]
        max_length = max([len(string) for string in valid_strings])
        longest_valid_strings = [string for string in valid_strings if len(string) == max_length]
        
        # self.memo[start] = longest_valid_strings
        return longest_valid_strings
