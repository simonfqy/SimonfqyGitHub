'''
Link: https://www.lintcode.com/problem/binary-number-with-alternating-bits/description
'''

# Uses bit operation.
class Solution:
    """
    @param n: a postive Integer
    @return: if two adjacent bits will always have different values
    """
    def hasAlternatingBits(self, n):
        # Write your code here
        number = n
        last_num = number & 1
        while number != 0:
            number = number >> 1
            new_last = number & 1
            if new_last == last_num:
                return False
            last_num = new_last
        return True

    
# 本参考程序来自九章算法，由 @九章算法助教团队 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param n: a postive Integer
    @return: if two adjacent bits will always have different values
    """
    """
    一个具有交替位的二进制数，我们把它右移一位后与原二进制数异或，得到的新二进制数每一位上都是1。
    把问题转化为了如何判断一个二进制数是否每一位全为1,这里我们采用的方法是将该二进制数+1后与原数进行与操作。
    """
    def hasAlternatingBits(self, n):
        # Write your code here
        n = n ^ (n>>1)
        return (n & n+1) == 0
