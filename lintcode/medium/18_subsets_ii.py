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
            subset = subset_so_far + [nums[i]]
            self.helper(nums, i + 1, subset)
            self.results.append(subset)
            
           
# My solution after reading https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/hui-su-sua-56e11/.
# The self.used array isn't needed here.
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
             we will sort your return value in output
    """
    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        self.results = []
        nums.sort()
        self.used = [False] * len(nums)
        self.dfs([], nums, 0)
        return self.results

    def dfs(self, subset, nums, ind):
        self.results.append(subset)
        for i in range(ind, len(nums)):
            if i > ind and nums[i] == nums[i - 1] and not self.used[i - 1]:
                continue
            self.used[i] = True
            self.dfs(subset + [nums[i]], nums, i + 1)
            self.used[i] = False            
            
         
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
        index_of_last_added_element = [-1]
        subsets = [[]]
        
        for i in range(len(nums)):
            size = len(subsets)
            for s in range(size):
                # index_of_last_added_element[s] is the index of the last element of subsets[s]. For example, consider nums is [1, 3, 3'], subsets[s] is [1],
                # then when i == 2, we don't want nums[2], which is 3', to be used to construct subset [1, 3'] and added to the subsets list. Because nums[1] 
                # was already used to construct [1, 3] which is already in the subsets list. This way we can avoid duplication.
                if i > 0 and nums[i] == nums[i - 1] and index_of_last_added_element[s] != i - 1:
                    continue
                subsets.append(subsets[s] + [nums[i]])
                index_of_last_added_element.append(i)
        
        return subsets
    
    
# My own solution, similar to 
# https://github.com/simonfqy/SimonfqyGitHub/blob/a8b3ea4391edff26add90f19faf5613e0a74d8cb/lintcode/medium/17_subsets.py#L65.
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        self.subsets = []
        self.helper(sorted(nums), 0, [], -1)
        return self.subsets
        
    def helper(self, nums, start, subset_so_far, last_element_ind):
        if start >= len(nums):
            self.subsets.append(subset_so_far)
            return
        # Don't include the current element
        self.helper(nums, start + 1, subset_so_far, last_element_ind)
        # Similar to https://github.com/simonfqy/SimonfqyGitHub/blob/1e7bd0f02fdd501d0fb4d3655202d7deef2924d3/lintcode/medium/18_subsets_ii.py#L74,
        # filters out the duplicate entries.
        if start > 0 and nums[start] == nums[start - 1] and last_element_ind != start - 1:
            return
        # Include the current element 
        self.helper(nums, start + 1, subset_so_far + [nums[start]], start)
        
# My own solution, using the standard BFS (with a queue).
from collections import deque
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        queue = deque([([], -1)])
        nums.sort()
        subset_list = []        
        while queue:
            subset, last_added_element_ind = queue.popleft()
            subset_list.append(subset)
            for i in range(len(nums)):       
                # Skip those elements which we already traversed.
                if i <= last_added_element_ind:
                    continue                
                # Get rid of duplicate results.
                if i > 0 and nums[i] == nums[i - 1] and last_added_element_ind != i - 1:
                    continue
                queue.append((subset + [nums[i]], i))
        return subset_list 
    
  
# Also my own solution, a more complicated and less desirable version of the solution above.
# Lesson learned: if we already have a last_added_element_ind variable to record the index, we don't need to compare values.
from collections import deque
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        queue = deque([([], -1)])
        nums.sort()
        subset_list = []        
        while queue:
            subset, last_added_element_ind = queue.popleft()
            subset_list.append(subset)
            for i in range(len(nums)):       
                # Here we compare values. It does the work, but not optimal (see the solution above).
                if subset and nums[i] < subset[-1]:
                    continue
                # If the last element of the subset equals the current value, we want to skip
                # the current number if we'll definitely get duplicate results. If last_added_element_ind is i - 1,
                # we might not get duplicate results (because we're adding an additional element with the same
                # value to the subset). If it is not i - 1, we'll definitely get duplicate results.
                # See https://github.com/simonfqy/SimonfqyGitHub/blob/238d3ab05e972ca9a0d5f853218a170c3a770477/lintcode/medium/18_subsets_ii.py#L75
                if subset and nums[i] == subset[-1] and last_added_element_ind != i - 1:
                    continue
                # In the last if condition, we allow the case with nums[i] == subset[-1] and last_added_element_ind == i - 1.
                # However, this may still lead to duplicates. 
                # Get rid of duplicate results.
                if i > 0 and nums[i] == nums[i - 1] and last_added_element_ind != i - 1:
                    continue
                queue.append((subset + [nums[i]], i))
        return subset_list 
