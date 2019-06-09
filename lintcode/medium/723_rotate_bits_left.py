'''
Link: https://www.lintcode.com/problem/rotate-bits-left/description
'''

# My own solution.
class Solution:
    """
    @param n: a number
    @param d: digit needed to be rorated
    @return: a number
    """
    def leftRotate(self, n, d):
        # write code here
        TOTAL_LEN = 32
        d = d % TOTAL_LEN
        leftmost_num = n >> (TOTAL_LEN - d)
        return (n << d) + leftmost_num
