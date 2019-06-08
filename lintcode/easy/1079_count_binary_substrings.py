'''
Link: https://www.lintcode.com/problem/count-binary-substrings/description
'''

# My own solution.
class Solution:
    """
    @param s: a string
    @return: the number of substrings
    """
    def countBinarySubstrings(self, s):
        # Write your code here
        count = 0
        for i in range(len(s)):
            exist_contiguous_substr = self.check_exist_contiguous(s[i:])
            if exist_contiguous_substr:
                count += 1
        return count
        
    def check_exist_contiguous(self, s):
        first_counter = 0
        second_counter = 0
        for char in s:
            if char == s[0]:
                if second_counter > 0:
                    return False
                first_counter += 1
            else:
                second_counter += 1
                if second_counter == first_counter:
                    return True
        return False
    
    
    
# 本参考程序来自九章算法，由 @九章算法助教团队 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
   def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        统计相邻连续的0和1的数量
        """
        n=len(s)
        res=0
        start=0
        lastcount=1
        for i in xrange(1,n):
            if s[i]!=s[i-1]:
                res+=1
                lastcount=i-start
                start=i
            else:
                if i-start<lastcount:
                    res+=1
        return res
