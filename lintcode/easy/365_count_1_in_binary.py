'''
Link: https://www.lintcode.com/problem/count-1-in-binary/description
'''
class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        # write your code here
        i = 0
        count = 0
        # The limit for integers set by Python, 32 binary digits. If you set it to 
        # (1 << i) <= num, it would be incorrect, since there are negative numbers, which has 1 on the
        # leftmost digit in the 32 binary values.
        while i < 32:
            count += ((1 << i) & num > 0)
            i += 1
        return count
