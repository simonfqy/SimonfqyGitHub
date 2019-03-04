'''
Link: https://www.lintcode.com/problem/fibonacci/description
'''

# There is a method using recursion with memoization, but I did not use it.
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        third = 0
        second = 0
        first = 0
        if n == 1:
            return first
        if n >= 2:
            second += 1
            if n == 2:
                return second
        for _ in range(2, n):
            third = second + first
            first = second
            second = third
        return third
