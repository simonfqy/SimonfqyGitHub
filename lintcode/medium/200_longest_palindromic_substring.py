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

'''
This solution enumerates the middle entry of each palindromic substring. It achieves a time complexity of O(n^2), because
it no longer performs is_palindrome() test on each possible length, thus removing 1 level of nested loop in the previous
solution. It is similar to a two-pointer solution.
'''  
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    
    def longestPalindrome(self, s):
        # write your code here
        if s is None:
            return ''
        self.start = 0
        self.longest = 0
        for middle in range(len(s)):
            # Enumerate the middle entry of palindromic substring
            self.get_palindromic_string(s, middle, middle)
            # Do the same thing for a possible even-length palindromic string.
            self.get_palindromic_string(s, middle, middle + 1)
            
        return s[self.start : (self.start + self.longest)]
    
    def get_palindromic_string(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Because left and right are overly incremented/decremented, we need to 
        # use the length previous to the last increment/decrement
        if self.longest < right - left - 1:
            self.longest = right - left - 1
            self.start = left + 1 
