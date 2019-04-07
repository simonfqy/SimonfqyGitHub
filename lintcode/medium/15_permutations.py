'''
Link: https://www.lintcode.com/problem/permutations/description
'''

# I came up with solution after watching half of the Jiuzhang video on this problem
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        output_list = []
        if nums is None:
            return output_list
        ind_availability = [True for _ in range(len(nums))]
        this_lvl_unavailable_inds = set()
        permutation = []
        self.dfs(nums, ind_availability, this_lvl_unavailable_inds, permutation,
            output_list)
        return output_list
        
        
    def dfs(self, nums, ind_availability, this_lvl_unavailable_inds, permutation,
        output_list):
        if len(permutation) == len(nums):
            output_list.append(permutation)
            return
        
        for i, num in enumerate(nums):
            if not ind_availability[i]:
                continue
            if i in this_lvl_unavailable_inds:
                continue
            perm = list(permutation)
            perm.append(num)
            ind_availability[i] = False
            # Go one level deeper
            self.dfs(nums, ind_availability, set(), perm, output_list)
            ind_availability[i] = True
            this_lvl_unavailable_inds.add(i)
