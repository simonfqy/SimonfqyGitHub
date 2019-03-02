'''
Link: https://www.lintcode.com/problem/single-number/description
It uses XOR operation, which is bitwise or. The operands in XOR are interchangeable, and 0^x = x, a^a = 0, hence the result.
Solution provided by Jiuzhang.com.
'''
class Solution:
    """
   @param A : an integer array
   @return : a integer
   """
    def singleNumber(self, A):
        # write your code here
        ans = 0;
        for x in A:
            ans = ans ^ x
        return ans
