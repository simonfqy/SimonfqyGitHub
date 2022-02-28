'''
Link: https://www.lintcode.com/problem/triangle/description
'''

# Correct, but causes time limit exceeded problem.
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        return self.minimum_triang(triangle, 0, 0)
        
    def minimum_triang(self, triangle, start_row, start_ind):
        if start_row >= len(triangle):
            return 0
        left_min = self.minimum_triang(triangle, start_row + 1, start_ind)
        right_min = self.minimum_triang(triangle, start_row + 1, start_ind + 1)
        return triangle[start_row][start_ind] + min(left_min, right_min)


# Correct but also exceeds time limit.
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        if len(triangle) <= 0:
            return None
        # Stack of coordinates of points.
        stack = [[0, 0]]
        node_values_on_the_path = []
        current_best = None
        current_sum = 0
        while stack:
            row, col = stack.pop()
            while row <= len(node_values_on_the_path) - 1:
                val_of_popped_node = node_values_on_the_path.pop()
                current_sum -= val_of_popped_node
            node_values_on_the_path.append(triangle[row][col])
            current_sum += triangle[row][col]
            if row == len(triangle) - 1:
                if current_best is None or current_sum < current_best:
                    current_best = current_sum
            else:
                stack.append([row + 1, col + 1])
                stack.append([row + 1, col])
        return current_best
    
    
# My own solution, uses Dynamic Programming.
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        if len(triangle) <= 0:
            return None
        sum_array = [None for _ in triangle]
        sum_array[0] = triangle[0][0]
        for row in triangle[1:]:
            n = len(row)
            sum_array[n - 1] = sum_array[n - 2] + row[n - 1]
            for i in range(n - 2, 0, -1):
                sum_array[i] = min(sum_array[i - 1], sum_array[i]) + row[i]
            sum_array[0] = sum_array[0] + row[0]
        return min(sum_array)
    
    
# DFS + memoization
# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        return self.divide_conquer(triangle, 0, 0, {})
        
    # 函数返回从 x, y 出发，走到最底层的最短路径值
    # memo 中 key 为二元组 (x, y)
    # memo 中 value 为从 x, y 走到最底层的最短路径值
    def divide_conquer(self, triangle, x, y, memo):
        if x == len(triangle):
            return 0
            
        # 如果找过了，就不要再找了，直接把之前找到的值返回
        if (x, y) in memo:
            return memo[(x, y)]

        left = self.divide_conquer(triangle, x + 1, y, memo)
        right = self.divide_conquer(triangle, x + 1, y + 1, memo)
        
        # 在 return 之前先把这次找到的最短路径值记录下来
        # 避免之后重复搜索
        memo[(x, y)] = min(left, right) + triangle[x][y]
        return memo[(x, y)]
    
    
# My own solution, uses DP. Has O(n^2) time complexity and O(n) space complexity.
from typing import (
    List,
)

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimum_total(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        n = len(triangle)
        dp = [0] * n
        prev_row = [0] * n
        for row_ind in range(n):
            row = triangle[row_ind]
            for col_ind in range(row_ind + 1):
                dp[col_ind] = row[col_ind]
                if col_ind == 0:
                    dp[col_ind] += prev_row[col_ind]
                    continue
                if col_ind == row_ind:
                    dp[col_ind] += prev_row[col_ind - 1]
                    continue
                dp[col_ind] += min(prev_row[col_ind - 1], prev_row[col_ind])
            if row_ind == n - 1:
                return min(dp)
            dp, prev_row = prev_row, dp

            
