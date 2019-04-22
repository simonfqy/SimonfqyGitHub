'''
Link: https://www.lintcode.com/problem/partition-array-ii/description
'''

# I did not completely come up with this solution correctly. I had to refer to the sort colors problem solution.
# TAKEAWAY lesson: if not sure, do things one step at a time. Use logic to eliminate impossible but confusing and
# annoying cases.
class Solution:
    """
    @param nums: an integer array
    @param low: An integer
    @param high: An integer
    @return: nothing
    """
    def partition2(self, nums, low, high):
        # write your code here
        if nums is None or len(nums) <= 1:
            return
        left, mid, right = 0, 0, len(nums) - 1
        while mid <= right:
            # The whole if-else block only traverses 1 step per iteration of the while loop.
            if nums[mid] < low:
                # Since the mid pointer traverses the array from the start, to this point, all entries
                # prior to mid are smaller than or equal to "high". What if after swapping nums[left] and 
                # nums[mid], the new nums[mid] is greater than high and since mid is now mid+1, the array
                # will be in the wrong order? This case will not happen, rest assured. 
                # WE SHOULD ALWAYS USE LOGIC TO ELIMINATE THE IMPOSSIBLE CASES.
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                # Naturally, move the middle pointer forward. 
                mid += 1
            elif nums[mid] > high:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
            else:
                mid += 1
        return

    
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

# 参考程序2
class Solution:
    # @param {int[]} nums an integer array
    # @param {int} low an integer
    # @param {int} high an integer
    # @return nothing
    def partition2(self, nums, low, high):
        # Write your code here
        left = 0
        right = len(nums) - 1

        # 首先把区间分为 < low 和 >= low 的两个部分 
        while left <= right:
            while left <= right and nums[left] < low:
                left = left + 1
            while left <= right and nums[right] >= low:
                right = right - 1
            if left <= right:
                nums[right],nums[left] = nums[left],nums[right]
                left = left + 1
                right = right - 1

        right = len(nums) - 1
        # 然后从 >= low 的部分里分出 <= high 和 > high 的两个部分
        while left <= right:
            while left <= right and nums[left] <= high:
                left = left + 1
            while left <= right and nums[right] > high:
                right = right - 1
            if left <= right:
                nums[right],nums[left] = nums[left],nums[right]
                left = left + 1
                right = right - 1
