'''
Link: https://www.lintcode.com/problem/o1-check-power-of-2/description
'''

# Using bit and to get the answer. O(1) time complexity.
class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        if n <= 0:
            return False
        return (n & (n - 1) == 0)
