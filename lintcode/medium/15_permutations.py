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
            # In fact we don't need this_lvl_unavailable_inds, since the elements in nums[] is
            # iterating in order, there is no chance that the next if block will be used.
            if i in this_lvl_unavailable_inds:
                continue
            perm = list(permutation)
            perm.append(num)
            ind_availability[i] = False
            # Go one level deeper
            self.dfs(nums, ind_availability, set(), perm, output_list)
            ind_availability[i] = True
            this_lvl_unavailable_inds.add(i)
            
            
# My own solution after 7 weeks of writing the previous solution.
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if nums is None or len(nums) <= 0:
            return [[]]
        output_list = []
        self.get_permutations(nums, [], output_list)
        return output_list
        
    def get_permutations(self, nums, subset, output_list):
        if len(subset) == len(nums):
            output_list.append(subset)
            return
        for number in nums:
            if number in set(subset):
                continue
            self.get_permutations(nums, subset + [number], output_list)
            

# My own iterative solution using BFS.
from collections import deque
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if nums is None or len(nums) <= 0:
            return [[]]
        output_list = []
        queue = deque([[]])
        self.get_permutations(nums, output_list, queue)
        return output_list
        
    def get_permutations(self, nums, output_list, queue):
        while queue:
            subset = queue.popleft()
            if len(subset) == len(nums):
                output_list.append(subset)
                continue
            for number in nums:
                if number in set(subset):
                    continue
                queue.append(subset + [number])

               
# Using iterative DFS.            
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if nums is None or len(nums) <= 0:
            return [[]]
        output_list = []
        stack = [[]]
        self.get_permutations(nums, output_list, stack)
        return output_list
        
    def get_permutations(self, nums, output_list, stack):
        while stack:
            subset = stack.pop()
            if len(subset) == len(nums):
                output_list.append(subset)
                continue
            for number in nums:
                if number in set(subset):
                    continue
                stack.append(subset + [number])
                
                
# This solution is from a student on jiuzhang.com.     
# 每次看nums中的一个元素，对之前结果集的每一个permutation，在所有可能的插入点（N个）插入当前元素。
# 比如nums是[1, 2, 3]，最初结果集是[[]]。看到1，结果集变为[[1]]，因为空list只有一个位置可以插入。 看到2，扩展为[[1, 2], [2, 1]，
# 因为[1]有两个位置可以插入。 看到3, 扩展为[[3, 1, 2], [1, 3, 2], [1, 2, 3], [3, 2, 1], [2, 3, 1], [2, 1, 3]]，因为上面的两种排列各有3个插入点。
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        results = [[]]
        for i, n in enumerate(nums):
            tmp = []
            for r in results:
                for j in range(0, i + 1):
                    tmp.append(r[:j] + [n] + r[j:])
            results = tmp
        return results
