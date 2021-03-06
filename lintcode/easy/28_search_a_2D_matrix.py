'''
Link: https://www.lintcode.com/problem/search-a-2d-matrix/description
'''

# This is my own solution.
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if target is None or matrix is None or not len(matrix) or not len(matrix[0]):
            return False
        sentinels = []
        for i in range(len(matrix)):
            sentinels.append(matrix[i][0])
        if len(matrix[i]) > 1:
            sentinels.append(matrix[i][len(matrix[i]) - 1])
        
        start, end, found = self.do_binary_search(sentinels, target)
        if found:
            return True
        
        if sentinels[start] == target or sentinels[end] == target:
            return True
        
        row_ind = 0
        if sentinels[start] > target:
            row_ind = start - 1
        elif sentinels[end] > target:
            row_ind = start
        else:
            row_ind = end
        if row_ind < 0 or row_ind >= len(matrix):
            return False
        
        row_to_inspect = matrix[row_ind]
        start, end, found = self.do_binary_search(row_to_inspect, target)
        if found:
            return True
        return row_to_inspect[start] == target or row_to_inspect[end] == target
                        
            
    def do_binary_search(self, list_to_search, target):
        start, end = 0, len(list_to_search) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if list_to_search[mid] > target:
                end = mid
            elif list_to_search[mid] == target:
                return start, end, True
            else:
                start = mid
        return start, end, False    
    

# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
            
        n, m = len(matrix), len(matrix[0])
        start, end = 0, n * m - 1
        while start + 1 < end:
            mid = (start + end) / 2
            x, y = mid / m, mid % m
            if matrix[x][y] < target:
                start = mid
            else:
                end = mid
        x, y = start / m, start % m
        if matrix[x][y] == target:
            return True
        
        x, y = end / m, end % m
        if matrix[x][y] == target:
            return True
        
        return False
