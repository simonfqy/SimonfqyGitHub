'''
Link: https://www.lintcode.com/problem/subsets/description
'''

# This is a version in which every node in the tree should be included in the final output.
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        subset_list = [[]]
        if nums is None or len(nums) <= 0:
            return subset_list
        nums.sort()
        subset_list.extend(self.get_subset_list(nums, []))
        return subset_list
        
    # Recursion. Uses DFS all the way to the bottom.
    def get_subset_list(self, numbers, prefix):
        if len(numbers) <= 0:
            return None
        subset_list = []
        for i in range(len(numbers)):
            prefix_and_this_value_list = prefix + [numbers[i]]
            subset_list.append(prefix_and_this_value_list)
            branch_list = self.get_subset_list(numbers[i+1:], prefix_and_this_value_list)
            if branch_list is not None:
                subset_list.extend(branch_list)
        return subset_list
        
    # A slightly modified version compared to the previous one.
    def get_subset_list(self, numbers, prefix):
        subset_list = []
        for i, this_num in enumerate(numbers):
            prefix_and_this_value_list = prefix + [this_num]
            subset_list.append(prefix_and_this_value_list)
            if i + 1 >= len(numbers):
                break       
            subset_list.extend(self.get_subset_list(numbers[i+1:], prefix_and_this_value_list))
        return subset_list

# Same idea, but better, more succinct solution.
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here  
        nums.sort()
        subset_list = []
        self.get_subset_list(nums, 0, [], subset_list)
        return subset_list
    
    def get_subset_list(self, nums, curr_ind, prefix, subset_list):
        # All the prefixes must be appended to subset_list, since they are all valid and non-overlapping.
        subset_list.append(prefix)
        for i in range(curr_ind, len(nums)):
            self.get_subset_list(nums, i + 1, prefix + [nums[i]], subset_list)
    
    
# A solution using the leaf nodes only.
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here  
        nums.sort()
        subset_list = []
        self.get_subset_list(nums, 0, [], subset_list)
        return subset_list        
    
    def get_subset_list(self, nums, curr_ind, prefix, subset_list):
        if curr_ind >= len(nums):
            subset_list.append(prefix)
            return 
        # Do not include the current element
        self.get_subset_list(nums, curr_ind + 1, prefix, subset_list)
        # Include the current element.
        self.get_subset_list(nums, curr_ind + 1, prefix + [nums[curr_ind]], subset_list)
        
       
# Using BFS.
from collections import deque
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here  
        queue = deque([[]])
        return self.get_subset_list(sorted(nums), queue)
    
    def get_subset_list(self, nums, queue):
        subset_list = []
        while queue:
            subset = queue.popleft()            
            subset_list.append(subset)
            for number in nums:
                if subset and number <= subset[-1]:
                    continue
                queue.append(subset + [number])
        return subset_list
    

# Solution from Jiuzhang.com. Makes use of bitwise operation. Does not apply to subsets II, in which duplicate
# elements exist.
class Solution:
    def subsets(self, nums):
        result = []
        n = len(nums)
        nums.sort()

        # 1 << n is 2^n
        # each subset equals to an binary integer between 0 .. 2^n - 1
        # 0 -> 000 -> []
        # 1 -> 001 -> [1]
        # 2 -> 010 -> [2]
        # ..
        # 7 -> 111 -> [1,2,3]
        for i in range(1 << n):
            subset = []
            for j in range(n):
                if (i & (1 << j)) != 0:
                    subset.append(nums[j])
            result.append(subset)
        return result
    
    
# Iterative BFS solution. Similar to 
# https://github.com/simonfqy/SimonfqyGitHub/blob/238d3ab05e972ca9a0d5f853218a170c3a770477/lintcode/medium/18_subsets_ii.py#L59.
# This solution is less generic than the BFS solution above, but more succinct. It only uses one array, namely all_subsets, and
# do not need to use a separate deque. The functionality of deque is accomplished by traversing through all_subsets. It is taking
# advantage of the property that, all the subsets (including leaf or non-leaf nodes in the tree) should be added to the final list
# and we don't need to pop them. So all_subsets only appends and never pops.
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here  
        all_subsets = [[]]
        nums.sort()
        for i in range(len(nums)):
            size = len(all_subsets)
            for s in range(size):
                subset = all_subsets[s]
                all_subsets.append(subset + [nums[i]])
        return all_subsets  
