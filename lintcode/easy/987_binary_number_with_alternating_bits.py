'''
Link: https://www.lintcode.com/problem/binary-number-with-alternating-bits/description
'''

# Uses bit operation.
class Solution:
    """
    @param n: a postive Integer
    @return: if two adjacent bits will always have different values
    """
    def hasAlternatingBits(self, n):
        # Write your code here
        number = n
        last_num = number & 1
        while number != 0:
            number = number >> 1
            new_last = number & 1
            if new_last == last_num:
                return False
            last_num = new_last
        return True
