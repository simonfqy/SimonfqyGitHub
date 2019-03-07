'''
Link: https://www.lintcode.com/problem/search-in-rotated-sorted-array/description
'''

# This is my own implementation.
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if A is None or not len(A):
            return -1
        
        # Idea: first get the index of the lowest value, then do binary search in the two segments.
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > A[start]:
                start = mid
            else:
                end = mid
                
        if A[start] < A[end]:
            ind_smallest_value = start
        else:
            ind_smallest_value = end
        
        ind_return = self.binary_search(A, target, ind_smallest_value, len(A) - 1)
        if ind_return != -1:
            return ind_return
        if ind_smallest_value > 0:
            ind_return = self.binary_search(A, target, 0, ind_smallest_value - 1)
        return ind_return
        
        
    def binary_search(self, A, target, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > target:
                end = mid
            elif A[mid] == target:
                return mid
            else:
                start = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1

  
# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

# 用一次二分法
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        if not A:
            return -1
            
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= A[start]:
                if A[start] <= target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid
                    
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
    
    
# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

# 用两次二分法
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        if not A:
            return -1
            
        index = self.find_min_index(A)
        if A[index] <= target <= A[-1]:
            return self.binary_search(A, index, len(A) - 1, target)
        return self.binary_search(A, 0, index - 1, target)
        
    def find_min_index(self, A):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < A[end]:
                end = mid
            else:
                start = mid
        
        if A[start] < A[end]:
            return start
        return end

    def binary_search(self, A, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
