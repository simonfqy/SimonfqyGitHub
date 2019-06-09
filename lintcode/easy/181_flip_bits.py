'''
Link: https://www.lintcode.com/problem/flip-bits/description
'''

class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        # Cut off at 4 bytes (32 bits), since in Python, the negative numbers have infinite leading ones.
        a = ((1 << 32) - 1) & a
        b = ((1 << 32) - 1) & b
        c = a ^ b
        count = 0
        while c != 0:
            c &= c - 1
            count += 1
        return count
