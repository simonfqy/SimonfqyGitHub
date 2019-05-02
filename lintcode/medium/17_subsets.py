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
