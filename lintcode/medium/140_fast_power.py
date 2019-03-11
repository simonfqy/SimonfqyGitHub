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
      
    
# My own non-recursive solution.
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        # Try non-recursive version
        if n == 0:
            return int(1 % b)
        ret_value = int(a % b)
        n -= 1
        while n > 0:
            exponent = 1
            inner_mod = int(a % b)
            while exponent <= n / 2:
                inner_mod = int(pow(inner_mod, 2) % b)
                exponent *= 2
            ret_value = int((inner_mod * (ret_value % b)) % b)
            n -= exponent
        return ret_value
