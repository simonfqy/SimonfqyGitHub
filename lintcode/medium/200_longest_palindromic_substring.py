'''
Link: https://www.lintcode.com/problem/longest-palindromic-substring/description

'''
# This is a O(n^3) time complexity brute-force solution.
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def is_palindrome(self, s, left, right):
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        
    def longestPalindrome(self, s):
        # write your code here
        longest_palindrome = ''
        for start_ind in range(len(s)):
            if len(longest_palindrome) >= len(s) - start_ind:
                break
            for offset in range(len(s)-start_ind):
                substr = s[start_ind: (start_ind + offset + 1)]
                if self.is_palindrome(s, start_ind, start_ind + offset):
                    if len(substr) > len(longest_palindrome):
                        longest_palindrome = substr
        return longest_palindrome
