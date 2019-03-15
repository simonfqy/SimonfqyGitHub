'''
https://www.lintcode.com/problem/rotate-string/description
'''

# My own solution.
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        if offset == 0:
            return
        if str is None or len(str) <= 1:
            return
        offset = offset % len(str)
        self.reverse(str, 0, len(str) - 1)
        self.reverse(str, 0, offset - 1)
        self.reverse(str, offset, len(str) - 1)
        
    def reverse(self, str, start, end):
        while start < end:
            temp = str[start]
            str[start] = str[end]
            str[end] = temp
            start += 1
            end -= 1
            
            
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

# This solution is not so good. It does not have constant space complexity.
class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
        # write you code here
        if len(s) > 0:
            offset = offset % len(s)
            
        temp = (s + s)[len(s) - offset : 2 * len(s) - offset]

        for i in xrange(len(temp)):
            s[i] = temp[i]
