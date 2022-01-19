'''
Link: https://www.lintcode.com/problem/517
'''

# My own solution. Not very elegant, has two special condition checks.
class Solution:
    """
    @param num: An integer
    @return: true if num is an ugly number or false
    """
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        expected_prime_factors = [2, 3, 5]
        divisible = True
        while divisible:
            divisible = False
            for prime_factor in expected_prime_factors:
                if num % prime_factor == 0:
                    divisible = True
                    num /= prime_factor
                    break
            
        return num == 1
      
      
