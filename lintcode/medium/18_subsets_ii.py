'''
Link: https://www.lintcode.com/problem/subsets-ii/description
'''

# My own solution.
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        
        if nums is None or len(nums) <= 0:
            return [[]]
        nums.sort()
        subset_list = []
        self.get_subset_list(nums, 0, [], subset_list)
        return subset_list
        
    def get_subset_list(self, nums, curr_ind, prefix, subset_list):
        # All the prefixes should be appended since they are all what we want.
        subset_list.append(prefix)
        for i in range(curr_ind, len(nums)):
            # Make sure that all "sibling" nodes are different, duplicates are prevented.
            if i > curr_ind and nums[i] == nums[i - 1]:
                continue
            self.get_subset_list(nums, i + 1, prefix + [nums[i]], subset_list)
      
    
# My own solution after 2 years. Similar to the one above, but more concise.
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        self.results = [[]]
        self.helper(sorted(nums), 0, [])
        return self.results
        
    def helper(self, nums, start, subset_so_far):
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            subsets = subset_so_far + [nums[i]]
            self.helper(nums, i + 1, subsets)
            self.results.append(subsets)
            
         
# An iterative solution.
# 本参考程序来自九章算法，由 @刘钟泽 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        nums.sort()
        subsets = [[]]
        indexes = [-1]  # 记录subsets中每个集合结尾元素的下标
        
        for i in range(len(nums)):
            size = len(subsets)
            for s in range(size):
                if i > 0 and nums[i] == nums[i-1] and indexes[s] != i-1:
                    continue  # 去重，如果有重复数字出现，只有前上一个数字选了才能选当前数字
                subsets.append(list(subsets[s]))
                subsets[-1].append(nums[i])
                indexes.append(i)
        
        return subsets
