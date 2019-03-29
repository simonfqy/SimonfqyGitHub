'''
Link: https://www.lintcode.com/problem/greatest-common-divisor/description
'''

# Based on the solution in Jiuzhang.com. Euclid's algorithm.
class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a, b):
        # write your code here
        big, small = a, b
        if big < small:
            big, small = b, a
        if small != 0:
            return self.gcd(small, big % small)
        else:
            return big
