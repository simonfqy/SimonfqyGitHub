'''
Link: https://www.lintcode.com/problem/sort-letters-by-case/description
'''

class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        # write your code here
        if chars is None or len(chars) < 1:
            return
        low_ptr, upp_ptr = 0, len(chars) - 1
        while low_ptr < upp_ptr:
            while low_ptr < upp_ptr and chars[low_ptr].islower():
                low_ptr += 1
            while low_ptr < upp_ptr and chars[upp_ptr].isupper():
                upp_ptr -= 1
            if low_ptr < upp_ptr:
                chars[low_ptr], chars[upp_ptr] = chars[upp_ptr], chars[low_ptr]
                low_ptr += 1
                upp_ptr -= 1
        return
