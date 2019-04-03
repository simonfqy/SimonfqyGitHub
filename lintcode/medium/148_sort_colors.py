'''
Link: https://www.lintcode.com/problem/sort-colors/description
'''

# My solution based on the teachings from Jiuzhang.com.
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if len(nums) <= 0:
            return
        left, right = 0, len(nums) - 1
        middle = 0
        while middle <= right:
            if nums[middle] == 0:
                nums[left], nums[middle] = nums[middle], nums[left]
                left += 1
                middle += 1
            elif nums[middle] == 2:
                nums[right], nums[middle] = nums[middle], nums[right]
                right -= 1
            else:
                middle += 1
        return
    
    
# This solution is not as good since it involves traversing the array twice.   
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, A):
        index = self.sort(A, 0, 0)
        self.sort(A, 1, index)
        
    def sort(self, A, flag, index):
        start, end = index, len(A) - 1
        while start <= end:
            while start <= end and A[start] == flag:
                start += 1
            while start <= end and A[end] != flag:
                end -= 1
            if start <= end:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
        return start
