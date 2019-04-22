'''
Link: https://www.lintcode.com/problem/move-zeroes/description
'''

# My own solution.
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        if nums is None or len(nums) <= 1:
            return
        left, right = 0, 1
        while right < len(nums):
            while right < len(nums) and nums[left] != 0:
                left += 1
                right += 1
            while right < len(nums) and nums[right] == 0:
                right += 1
            if right < len(nums):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
        return

    
# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

# This method ensures the minimum number of write operations.
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        if nums is None or len(nums) <= 1:
            return
        left, right = 0, 0
        # Since the right >= left always holds, there is no need to keep a list of nonzero elements
        # in the memory: we simply overwrite the nums[left] entries on the fly and no anomalies will occur.
        while right < len(nums):
            if nums[right] != 0:
                if left != right:
                    nums[left] = nums[right]
                left += 1
            right += 1
            
        # Overwrite the last few entries with zeroes.
        while left < len(nums):
            nums[left] = 0
            left += 1
        return
