'''
https://www.lintcode.com/problem/rotate-string/description
'''

# My own solution.
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        if offset == 0:
            return
        if str is None or len(str) <= 1:
            return
        offset = offset % len(str)
        self.reverse(str, 0, len(str) - 1)
        self.reverse(str, 0, offset - 1)
        self.reverse(str, offset, len(str) - 1)
        
    def reverse(self, str, start, end):
        while start < end:
            temp = str[start]
            str[start] = str[end]
            str[end] = temp
            start += 1
            end -= 1
