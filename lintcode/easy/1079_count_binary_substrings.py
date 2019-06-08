'''
Link: https://www.lintcode.com/problem/count-binary-substrings/description
'''

# My own solution.
class Solution:
    """
    @param s: a string
    @return: the number of substrings
    """
    def countBinarySubstrings(self, s):
        # Write your code here
        count = 0
        for i in range(len(s)):
            exist_contiguous_substr = self.check_exist_contiguous(s[i:])
            if exist_contiguous_substr:
                count += 1
        return count
        
    def check_exist_contiguous(self, s):
        first_counter = 0
        second_counter = 0
        for char in s:
            if char == s[0]:
                if second_counter > 0:
                    return False
                first_counter += 1
            else:
                second_counter += 1
                if second_counter == first_counter:
                    return True
        return False
