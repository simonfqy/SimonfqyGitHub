'''
Link: https://www.lintcode.com/problem/1171/
'''

# Solution slightly modified from the one from jiuzhang.com.
# mirroring函数构造回文序列，将传入的数字通过除法除half去除掉后半部分(例如121->12->120)，其中i控制为传入数字的一半，加上m%half可以补充去除的后半部分(120+1->121)。
# 每次将传入的字符串转化为整数，例如123，构造出三个数字a // half * half（120），b - (half // 10 if (half > 1) else 1 )(119)，b + half(130)。
# 由此可以得到的三个数字可以构造出最接近给出字符串的回文串。因为这些数字只是稍大或者稍小于原数字。
# 每次进行筛选保存结果即可。
class Solution:
    """
    @param n: a positive integer represented by string
    @return:  the closest integer which is a palindrome
    """
    def nearest_palindromic(self, n: str) -> str:
        number, res = int(n), 0
        half = int(10 ** (len(n) // 2))
        starting_num = number // half * half
        candidates = [starting_num, starting_num - (half // 10 if half > 1 else 1), starting_num + half]
        for cand in candidates:
            cand = self.mirroring(cand)
            if cand == number:
                continue
            if abs(res - number) > abs(cand - number) or (abs(res - number) == abs(cand - number) and cand < res):
                res = cand
        return str(res)

    def mirroring(self, candidate):        
        candidate_str = str(candidate)
        half = int(10 ** (len(candidate_str) // 2))
        reversed_num = int(candidate_str[::-1])        
        return candidate // half * half + reversed_num % half
      
      
