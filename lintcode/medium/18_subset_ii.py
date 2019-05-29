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
