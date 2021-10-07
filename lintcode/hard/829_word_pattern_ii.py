'''
https://www.lintcode.com/problem/829/
'''

# My own solution. Took quite some effort to debug and find the correct answer. You can see the learnings in the inline comments.
# It is DFS with recursion. 
class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        return self.helper(pattern, str, dict())

    def helper(self, pattern, str, pattern_char_to_string):
        if len(pattern) > len(str):
            return False
        if pattern == "" and str == "":
            return True
        if pattern == "" or str == "":
            return False
        if pattern[0] in pattern_char_to_string:
            candidate_matching_string = pattern_char_to_string[pattern[0]]
            if str[:len(candidate_matching_string)] != candidate_matching_string:
                return False
            return self.helper(pattern[1:], str[len(candidate_matching_string):], pattern_char_to_string)
        first_letter_in_pattern = pattern[0]
        # NOTE: we should always use a copy like done here for variables to be passed to the next DFS level. Otherwise we 
        # might incur undesired side effects.
        new_pattern_dict = dict(pattern_char_to_string)
        for i in range(len(str) - len(pattern) + 1):            
            candidate_string_matching_letter = str[:i + 1]
            # This check is necessary, otherwise we can't ensure that there is a bijection. For example, pattern "ab" should not
            # match string "aa", but without this check, it will return True.
            if candidate_string_matching_letter in set(new_pattern_dict.values()):
                continue
            new_pattern_dict[first_letter_in_pattern] = candidate_string_matching_letter
            if self.helper(pattern[1:], str[len(candidate_string_matching_letter):], new_pattern_dict):
                return True
        return False
