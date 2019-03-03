'''
Link: https://www.lintcode.com/problem/valid-palindrome/description

'''

# Inspired by the solution on Jiuzhang.com I read 2 months ago.
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        if s is None:
            return False
        left = 0
        right = len(s) - 1
        while left <= right:
            while not s[left].isalnum() and left < len(s) - 1:
                left += 1
            while not s[right].isalnum() and right > 0:
                right -= 1
            if left > right:
                break
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
    
# Wrote this version after reading the version on Jiuzhang.com immediately.
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        if s is None:
            return False
        left = 0
        right = len(s) - 1
        # Note: all the '<=' appearing in the subsequent code can be changed to '<',
        # since if left == right, it is no doubt that the s[left].lower() == s[right].lower().
        while left <= right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1
            if left <= right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
