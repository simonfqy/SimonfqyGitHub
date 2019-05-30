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
            
            
# This solution is provided by Jiuzhang.com. It also works.
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
        
        for i, num in enumerate(nums):
            if not ind_available[i]:
                continue
            # The previous element is identical to the current one, and the previous is not
            # used in this branch of the tree. The current branches' results must be duplicates of
            # what has already been produced.
            if i > 0 and num == nums[i - 1] and ind_available[i - 1]:
                continue
            perm = list(permutation)
            perm.append(num)
            ind_available[i] = False
            self.dfs(nums, ind_available, perm, output_list)
            ind_available[i] = True
            
            
# Inspired by Jiuzhang.com.
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
        used = [False for _ in nums]
        self.get_permutations(nums, [], used, output_list)
        return output_list
        
    def get_permutations(self, nums, subset, used, output_list):
        if len(subset) == len(nums):
            output_list.append(subset)
            return
        for i, number in enumerate(nums):
            # Make sure that the used elements are not duplicated.
            if used[i]:
                continue
            # Make sure that we will not choose the duplicated elements: the previous ones of such duplicated
            # elements must all appear, if they don't appear, it will result in duplications and such cases 
            # should be filtered out.
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            self.get_permutations(nums, subset + [number], used, output_list)
            # Restore the original array. Essentially backtracking.
            used[i] = False
