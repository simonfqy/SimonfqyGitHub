'''
Link: https://www.lintcode.com/problem/828
'''

# My own solution. It is a pretty straightforward problem, the time complexity and space complexity are both O(n), where
# n is the size of pattern or number of words in teststr.
class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        test_str_list = teststr.split(' ')
        pattern_list = list(pattern)
        pattern_char_to_string = dict()
        if len(pattern_list) != len(test_str_list):
            return False
        for i in range(len(pattern_list)):
            letter = pattern_list[i]
            curr_test_str = test_str_list[i]
            if letter in pattern_char_to_string:
                if curr_test_str != pattern_char_to_string[letter]:
                    return False
            else:
                if curr_test_str in set(pattern_char_to_string.values()):
                    return False
                pattern_char_to_string[letter] = curr_test_str
        return True
