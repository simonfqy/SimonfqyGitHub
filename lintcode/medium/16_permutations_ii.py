'''
Link: https://www.lintcode.com/problem/permutations-ii/description
'''

# My own solution after solving the simple permutations.
class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        output_list = []
        if nums is None:
            return output_list
        nums.sort()
        ind_available = [True for _ in nums]
        permutation = []
        self.dfs(nums, ind_available, permutation, output_list)
        return output_list
        
        
    def dfs(self, nums, ind_available, permutation, output_list):
        if len(permutation) == len(nums):
            output_list.append(permutation)
            return
        
        this_level_exclude = set()
        for i, num in enumerate(nums):
            if not ind_available[i]:
                continue
            if num in this_level_exclude:
                continue
            perm = list(permutation)
            perm.append(num)
            this_level_exclude.add(num)
            ind_available[i] = False
            self.dfs(nums, ind_available, perm, output_list)
            ind_available[i] = True
