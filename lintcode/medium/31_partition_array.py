'''
Link: https://www.lintcode.com/problem/partition-array/description
'''

# My own solution
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if len(nums) <= 0:
            return 0
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] < k:
                left += 1
            while left < right and k <= nums[right]:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        # compare the values
        if nums[left] >= k:
            return left
        if nums[right] >= k:
            return right
        return right + 1

    
    
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        start, end = 0, len(nums) - 1
        while start <= end:
            while start <= end and nums[start] < k:
                start += 1
            while start <= end and nums[end] >= k:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return start
