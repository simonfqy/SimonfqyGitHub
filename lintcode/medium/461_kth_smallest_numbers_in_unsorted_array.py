'''
Link: https://www.lintcode.com/problem/kth-smallest-numbers-in-unsorted-array/description
'''

# My own solution after some painstaking debugging process.
class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        if k > len(nums) or k < 1:
            return None
        left, right = 0, len(nums) - 1
        return self.quick_select(k - 1, nums, left, right)
        
        
    def quick_select(self, k, nums, start, end):
        left, right = start, end
        # Initially I set the following to right - left <= 1, which would occasionally return wrong results.
        if right <= left:
            return nums[k]
        pivot = nums[(left + right) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            # Initially I set the second condition to nums[right] >= pivot, which could cause infinite loop
            # if we have k = 3 and [3, 4, 1, 2, 5] as the input. So we must have > or <, no =.
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
        if k <= right:
            return self.quick_select(k, nums, start, right)
        if k >= left:
            return self.quick_select(k, nums, left, end)
        return nums[k]
    
    
# 本参考程序来自九章算法，由 @九章算法助教团队 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        return self.quickSelect(nums, 0, len(nums) - 1, k - 1)
    
    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        
        left, right = start, end
        pivot = nums[(left + right) // 2]
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        if right >= k and start <= right:
            return self.quickSelect(nums, start, right, k)
        elif left <= k and left <= end:
            return self.quickSelect(nums, left, end, k)
        else:
            return nums[k]
