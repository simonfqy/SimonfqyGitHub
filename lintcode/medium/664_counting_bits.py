'''
Link: https://www.lintcode.com/problem/counting-bits/description
'''

# Uses Dynamic Programming. The relationship is hard to notice at first, but easy to take advantage of.
class Solution:
    """
    @param num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    """
    def countBits(self, num):
        # write your code here
        answer = [0]
        for i in range(1, num + 1):
            if i % 2 == 0:
                number = answer[i//2]
            else:
                number = answer[i - 1] + 1
            answer.append(number)
        return answer
    
    
# Let dp[i] denote the number of ones in i's binary representation. We have dp[i] = dp[i >> 1] + i % 2,
# which is actually identical to the previous solution.
# 本参考程序来自九章算法，由 @九章算法助教团队 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    """
    def countBits(self, num):
        # write your code here
        f = [0] * (num + 1)
        for i in range(1, num+1):
            f[i] = f[i & i-1] + 1
        return f
