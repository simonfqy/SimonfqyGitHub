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
            
            
# Follow up: using iterative solution. Much more cumbersome.
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
        stack = [([], [False for _ in nums])]
        self.get_permutations(nums, [], output_list, stack)
        return output_list
        
    def get_permutations(self, nums, subset, output_list, stack):
        
        while stack:
            subset, used_arr = stack.pop()
            # Deep copy the used_arr.
            used = list(used_arr)
            if len(subset) == len(nums):
                output_list.append(subset)
                continue
            
            for i, number in enumerate(nums):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                # Using list(used) instead of raw "used", since the array "used" will soon be overwritten,
                # we want to keep a deep copy, not a shallow copy.
                stack.append((subset + [number], list(used)))
                # Overwrite it back to False for backtracking.
                used[i] = False
                
         
# Another iterative solution using the 190. next permutation ii.
class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        if nums is None or len(nums) <= 0:
            return [[]]
        output_list = []
        nums.sort()
        output_list.append(list(nums))
        while self.get_ind(nums) > 0:
            self.next_permute(nums)
            output_list.append(list(nums))
        return output_list
        
    def get_ind(self, nums):
        for i in range(len(nums) - 1, -1, -1):
            if i > 0 and nums[i] <= nums[i - 1]:
                continue
            return i
            
    def next_permute(self, nums):
        ind_start_reverse = self.get_ind(nums)
        if ind_start_reverse > 0:
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] > nums[ind_start_reverse - 1]:
                    nums[i], nums[ind_start_reverse - 1] = nums[ind_start_reverse - 1], nums[i]
                    break
        self.reverse_list(nums, ind_start_reverse, len(nums) - 1)
        return
    
    def reverse_list(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
            
# Using DFS. Conceptually similar to the solutions I provided above, but we're also including a list of indices to de-duplicate.
class Solution:
    """
    @param nums: A list of integers
    @return: A list of unique permutations
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.helper(sorted(nums), [], [], results)
        return results

    def helper(self, nums, perm, perm_indices, results):
        if len(perm) == len(nums):
            results.append(perm)
            return
        visited = set()
        for i in range(len(nums)):
            if i in perm_indices:
                continue
            # This is not a very elegant way of deduplication. A better way is to decide using the following condition:
            # i > 0 and nums[i] == nums[i - 1] and i - 1 not in perm_indices.
            if tuple(perm + [nums[i]]) in visited:
                continue
            visited.add(tuple(perm + [nums[i]]))
            self.helper(nums, perm + [nums[i]], perm_indices + [i], results)
            
            
# DFS using perm_indices to deduplicate. Similar to the one above but more elegant.
from typing import (
    List,
)
class Solution:
    """
    @param nums: A list of integers
    @return: A list of unique permutations
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.helper(sorted(nums), [], [], results)
        return results

    def helper(self, nums, perm, perm_indices, results):
        if len(perm) == len(nums):
            results.append(perm)
            return
        for i in range(len(nums)):
            if i in perm_indices:
                continue
            if i > 0 and nums[i] == nums[i - 1] and i - 1 not in perm_indices:
                continue
            self.helper(nums, perm + [nums[i]], perm_indices + [i], results)   
            
            
# My own DFS solution after reading https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/hui-su-sua-c26da/.
# Similar to the solution above, but more elegant. Uses a list "used" rather than perm_indices.
class Solution:
    """
    @param nums: A list of integers
    @return: A list of unique permutations
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.permutations = []
        self.used = [False for _ in nums]
        self.dfs(nums, [])
        return self.permutations
    
    def dfs(self, nums, prefix):
        if len(prefix) == len(nums):
            self.permutations.append(prefix)
            return
        for i, num in enumerate(nums):
            if self.used[i] or (i > 0 and num == nums[i - 1] and not self.used[i - 1]):
                continue
            self.used[i] = True
            self.dfs(nums, prefix + [num])
            self.used[i] = False
            
            
# BFS. Also uses a set to store the visited combinations. Note the place where it is used and the way we traverse the queue. 
# Likewise, we actually don't need to use the visited set to deduplicate. Simply using i > 0 and nums[i] == nums[i - 1] and i - 1 not in perm_indices
# condition will work.
from collections import deque
class Solution:
    """
    @param nums: A list of integers
    @return: A list of unique permutations
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        queue = deque([([], [])])        
        while queue:
            size = len(queue)
            visited = set()
            for _ in range(size):
                perm, perm_indices = queue.popleft()
                if len(perm) == len(nums):
                    results.append(perm)
                    break
                for i in range(len(nums)):
                    if i in perm_indices:
                        continue
                    if tuple(perm + [nums[i]]) in visited:                    
                        continue
                    visited.add(tuple(perm + [nums[i]]))
                    queue.append((perm + [nums[i]], perm_indices + [i])) 
        return results
    
  
# My own BFS solution after reading https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/hui-su-sua-c26da/.
# Similar to the latest DFS solution above.
from collections import deque
class Solution:
    """
    @param nums: A list of integers
    @return: A list of unique permutations
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.permutations = []
        queue = deque([([], set())])
        self.bfs(nums, queue)
        return self.permutations
    
    def bfs(self, nums, queue):
        while queue:
            prefix, used_ind = queue.popleft()
            if len(prefix) == len(nums):
                self.permutations.append(prefix)
                continue
            for i, num in enumerate(nums):
                if i in used_ind or (i > 0 and num == nums[i - 1] and i - 1 not in used_ind):
                    continue
                queue.append((prefix + [num], used_ind | {i}))
                
                
