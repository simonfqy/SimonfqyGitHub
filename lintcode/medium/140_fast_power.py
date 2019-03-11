'''
Link: https://www.lintcode.com/problem/fast-power/description
'''

# This is my own recursive solution. Won't get stack overflow error.
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        # Try recursive version
        if n <= 1:
            return int(pow(a, n) % b)
        if n % 2 == 1:
            return int(((a % b) * pow(self.fastPower(a, b, (n - 1) / 2), 2)) % b)
        else:
            return int((pow(self.fastPower(a, b, n/2), 2)) % b)
