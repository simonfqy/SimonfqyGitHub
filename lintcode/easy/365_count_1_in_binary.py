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
        # The integers have unlimited number of digits in Python, so we need to cut it off at 32 binary digits. 
        # If you set it to (1 << i) <= num, it would be incorrect, since there are negative numbers, which has infinite 
        # 1s on the left side.
        while i < 32:
            count += ((1 << i) & num > 0)
            i += 1
        return count
