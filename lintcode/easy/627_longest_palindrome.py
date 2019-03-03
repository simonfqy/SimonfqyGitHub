'''
Link: https://www.lintcode.com/problem/longest-palindrome/description
It seems we can't use the Counter() function from collections package.
'''

class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        letter_to_count = dict()
        for letter in s:
            if letter not in letter_to_count:
                letter_to_count[letter] = 0
            letter_to_count[letter] += 1
        total_length = 0
        exist_odd = False
        for letter in letter_to_count:
            count = letter_to_count[letter]
            if count % 2 == 0:
                total_length += count
            else:
                exist_odd = True
                total_length += count - 1
        total_length += exist_odd
        return total_length
