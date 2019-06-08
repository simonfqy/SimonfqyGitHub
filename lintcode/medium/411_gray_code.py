'''
Link: https://www.lintcode.com/problem/gray-code/description
'''
class Solution:
    """
    @param n: a number
    @return: Gray code
    """
    def grayCode(self, n):
        # write your code here
        # Use DFS.
        return self.get_gray_code(n, [0])
        
    def get_gray_code(self, n, gray_code_so_far):
        start_element = gray_code_so_far[-1]
        for i in range(n + 1):
            new_element = (1 << i) + start_element
            if new_element > 0 and new_element < 2**n and self.is_two_power(new_element ^ start_element) and \
                new_element not in set(gray_code_so_far):
                candidate_gray_code = self.get_gray_code(n, gray_code_so_far + [new_element])
                if len(candidate_gray_code) == 2**n:
                    return candidate_gray_code
        
            new_element = start_element - (1 << i)
            if new_element > 0 and new_element < 2**n and self.is_two_power(new_element ^ start_element) and \
                new_element not in set(gray_code_so_far):
                candidate_gray_code = self.get_gray_code(n, gray_code_so_far + [new_element])
                if len(candidate_gray_code) == 2**n:
                    return candidate_gray_code
        return gray_code_so_far                
            
    def is_two_power(self, number):
        count_one = 0
        while number != 0:
            if number & 1 == 1:
                count_one += 1
                if count_one > 1:
                    return False
            number = number >> 1
        return count_one == 1
    
    
# A more efficient solution, the new element can be determined prior to testing, saving some troubles.    
class Solution:
    """
    @param n: a number
    @return: Gray code
    """
    def grayCode(self, n):
        # write your code here
        # Use DFS.
        return self.get_gray_code(n, [0])
        
    def get_gray_code(self, n, gray_code_so_far):
        start_element = gray_code_so_far[-1]
        for i in range(n + 1):
            if (start_element >> i) & 1 == 0:
                new_element = (1 << i) + start_element
                if new_element > 0 and new_element < 2**n and \
                    new_element not in set(gray_code_so_far):
                    candidate_gray_code = self.get_gray_code(n, gray_code_so_far + [new_element])
                    if len(candidate_gray_code) == 2**n:
                        return candidate_gray_code
            else:
                new_element = start_element - (1 << i)
                if new_element > 0 and new_element < 2**n and \
                    new_element not in set(gray_code_so_far):
                    candidate_gray_code = self.get_gray_code(n, gray_code_so_far + [new_element])
                    if len(candidate_gray_code) == 2**n:
                        return candidate_gray_code
        return gray_code_so_far    
    
    
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param n: a number
    @return: Gray code
    """
    def grayCode(self, n):
        return [i ^ (i >> 1) for i in range(1 << n)]

################ 递归版本

class Solution:
    # @param {int} n a number
    # @return {int[]} Gray code
    def grayCode(self, n):
        if n == 0:
            return [0]
        
        result = self.grayCode(n - 1)
        seq = list(result)
        for i in reversed(result):
            seq.append((1 << (n - 1)) | i)
            
        return seq
