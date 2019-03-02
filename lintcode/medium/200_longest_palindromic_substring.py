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
     
    
'''
The following implementation uses Dynamic Programming (DP). I implemented it myself based on the idea that I was taught.
'''
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
    
    def fill_table_until_false(self, is_palindrome_tbl, s, n, start_ind_local, end_ind_local):
        while is_palindrome_tbl[start_ind_local][end_ind_local] == True:
            # Check whether the bigger substring that encloses it is palindromic
            start_ind_local -= 1
            end_ind_local += 1
            if start_ind_local >= 0 and end_ind_local < n and s[start_ind_local] == s[end_ind_local]:
                is_palindrome_tbl[start_ind_local][end_ind_local] = True
                if end_ind_local - start_ind_local + 1 > self.longest:
                    self.longest = end_ind_local + 1 - start_ind_local
                    self.start = start_ind_local
            else:
                break            
    
    def longestPalindrome(self, s):
        # write your code here
        if s is None:
            return ''
        n = len(s)
        is_palindrome_tbl = [[False]*n for _ in range(n)]
        self.longest = 0
        self.start = 0
        # Populate the first list in the table.
        for i in range(n):
            if self.is_palindrome(s, 0, i):
                is_palindrome_tbl[0][i] = True
                if i + 1 > self.longest:
                    self.longest = i + 1
            # Each character is palindromic with itself.
            is_palindrome_tbl[i][i] = True
        
        # Check whether there are palindromes longer than 1.
        for start_ind in range(n-1):
            for end_ind in range(start_ind, n):
                # Check whether those substrings with length 2 are actually palindromic. Otherwise
                # they will not be covered, and the program only checks odd-lengthed strings.
                if end_ind - start_ind == 1 and self.is_palindrome(s, start_ind, end_ind):
                    is_palindrome_tbl[start_ind][end_ind] = True
                    if 2 > self.longest:
                        self.longest = 2
                        self.start = start_ind
                # If a string s[start_ind][end_ind] is palindromic and has length > 2, then s[start_ind+1][end_ind-1]
                # must also be palindromic. It is not true the other way around. The following function takes care of
                # this scenario and check the possible palindromic substring by expanding the already palindromic 'kernel'.
                self.fill_table_until_false(is_palindrome_tbl, s, n, start_ind, end_ind)
                
        return s[self.start : self.longest + self.start]
    
'''
This solution uses Manacher's algorithm and is provided by Jiuzhang.com.
'''
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
   
    def longestPalindrome(self, s):
        # write your code here
       
        if not s:
            return ''

        # Using manacher's algorithm
        # abba => #a#b#b#a#
        chars = []
        for c in s:
            chars.append('#')
            chars.append(c)
        chars.append('#')
        
        n = len(chars)
        palindrome = [0] * n
        palindrome[0] = 1
        
        mid, longest = 0, 1
        for i in range(1, n):
            length = 1
            if mid + longest > i:
                mirror = mid - (i - mid)
                length = min(palindrome[mirror], mid + longest - i)

            while i + length < len(chars) and i - length >= 0:
                if chars[i + length] != chars[i - length]:
                    break;
                length += 1
            
            if length > longest:
                longest = length
                mid = i
            
            palindrome[i] = length
        
        # remove the extra #
        longest = longest - 1
        start = (mid - 1) // 2 - (longest - 1) // 2
        return s[start:start + longest]
