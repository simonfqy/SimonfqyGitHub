'''
Link: https://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array/description
'''

# I wrote this solution.
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        first_num = nums[0]
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if (nums[mid] > first_num):
                start = mid
            else:
                end = mid
        return min(first_num, nums[start], nums[end])
    
    
# The following two solutions are from Jiuzhang.com
# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        if not nums:
            return -1
            
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
                
        return min(nums[start], nums[end])
    
    
class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        if not nums:
            return -1
            
        start, end = 0, len(nums) - 1
        target = nums[-1]
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                end = mid
            else:
                start = mid
        return min(nums[start], nums[end])
    
