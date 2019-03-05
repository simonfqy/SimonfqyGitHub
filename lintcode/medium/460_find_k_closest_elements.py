'''
Link: https://www.lintcode.com/problem/find-k-closest-elements/description
'''

# I wrote this solution based on the idea taught in Jiuzhang online course. Did not refer to their solution.
import math
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        output_list = []
        if k <= 0 or A is None or not len(A):
            return output_list
        ind_closest = self.get_closest_ind(A, target)
        output_list.append(A[ind_closest])
        left = ind_closest
        right = ind_closest
        
        while len(output_list) < k:
            left_value = math.inf
            right_value = math.inf
            if left > 0:
                left_value = A[left - 1]
            if right < len(A) - 1:
                right_value = A[right + 1]
            if abs(left_value - target) <= abs(right_value - target):
                # Choose the left pointer at this point.
                left -= 1
                output_list.append(left_value)
            else:
                right += 1
                output_list.append(right_value)
        return output_list
            

    def get_closest_ind(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            elif A[mid] == target:
                end = mid
                return mid
            if A[mid] > target:
                end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        if abs(A[start] - target) <= abs(A[end] - target):
            return start
        else:
            return end
   

# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # 找到 A[left] < target, A[right] >= target
        # 也就是最接近 target 的两个数，他们肯定是相邻的
        right = self.find_upper_closest(A, target)
        left = right - 1
    
        # 两根指针从中间往两边扩展，依次找到最接近的 k 个数
        results = []
        for _ in range(k):
            if self.is_left_closer(A, target, left, right):
                results.append(A[left])
                left -= 1
            else:
                results.append(A[right])
                right += 1
        
        return results
    
    def find_upper_closest(self, A, target):
        # find the first number >= target in A
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        
        if A[start] >= target:
            return start
        
        if A[end] >= target:            
            return end
        
        # 找不到的情况
        return end + 1
        
    def is_left_closer(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target
