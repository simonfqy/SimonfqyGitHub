'''
Link: https://www.lintcode.com/problem/prime-factorization/description
'''
# This solution is inspired by the explanation on Jiuzhang.com
class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        prime_list = []
        if num is None or num <= 0:
            return prime_list
        ceiling = int(num ** 0.5) + 1
        for denom in range(2, ceiling):
            while num % denom == 0:
                num = num/denom
                prime_list.append(denom)
            if num == 1:
                return prime_list
        prime_list.append(int(num))
        return prime_list
