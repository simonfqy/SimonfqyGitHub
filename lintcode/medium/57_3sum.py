'''
Link: https://www.lintcode.com/problem/3sum/description
'''

# My own solution. Uses a running index and two pointers.
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        output_list = []
        if not numbers or len(numbers) < 3:
            return output_list
        numbers.sort()
        i = 0
        while i < len(numbers) - 2:
            left, right = i + 1, len(numbers) - 1
            while left < right:
                if numbers[left] + numbers[right] + numbers[i] == 0:
                    new_list = [numbers[i], numbers[left], numbers[right]]
                    output_list.append(new_list)
                    left += 1
                    right -= 1
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1
                    
                elif numbers[left] + numbers[right] + numbers[i] > 0:
                    right -= 1
                else:
                    left += 1
            i += 1
            while i < len(numbers) - 2 and numbers[i] == numbers[i - 1]:
                i += 1
                
        return output_list
    
    
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, nums):
        nums.sort()
        results = []
        length = len(nums)
        for i in range(0, length - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left, right = i + 1, length - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    results.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return results
    
    
# Answer from jiuzhang.com.
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        n = len(numbers)
        results = []
        for i, num in enumerate(numbers):
            if i > 0 and numbers[i - 1] == num:
                continue
            self.twoSum(numbers, i + 1, n - 1, -num, results)
        return results
        
    def twoSum(self, numbers, left, right, target, results):
        last_pair = (None, None)
        while left < right:
            if numbers[left] + numbers[right] == target:
                if (numbers[left], numbers[right]) != last_pair:
                    results.append([-target, numbers[left], numbers[right]])
                last_pair = (numbers[left], numbers[right])
                left += 1
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
