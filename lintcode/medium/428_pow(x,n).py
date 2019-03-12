'''
Link: https://www.lintcode.com/problem/powx-n/description
'''

# This solution is my own, but based on the 
# https://github.com/simonfqy/SimonfqyGitHub/blob/55e84e81334a2a924ee89e3c9364243e954aea3f/lintcode/medium/140_fast_power.py#L6
class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n == 0:
            return 1
        is_negative = (n < 0)
        n = abs(n)
        output = 1
        while n > 0:
            if n % 2 == 1:
                # The formulation of "binary number" is very helpful for understanding.
                output = x * output 
            x *= x
            n = n // 2
        if is_negative:
            output = 1.0/output
        return output
