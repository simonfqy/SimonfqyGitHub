'''
Link: https://www.lintcode.com/problem/10/
'''

# My own solution, recursive, using DFS. Time complexity is O(n*n!), space complexity is O(n*n!).
class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        letters = [char for char in str]
        permutations = []
        self.helper(sorted(letters), "", permutations)
        return permutations

    def helper(self, letters, combo_so_far, permutations):
        if len(letters) == 0:
            permutations.append(combo_so_far)
            return
        for i in range(len(letters)):
            if i > 0 and letters[i] == letters[i - 1]:
                continue
            self.helper(letters[:i] + letters[i + 1:], combo_so_far + letters[i], permutations)
            
            
# My own solution, using BFS, iterative. It should be correct, but hits space limited exceeded error.
# Time complexity is O(n*n!), space complexity is O(n*n!).
from collections import deque
class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        letters = [char for char in str]
        letters.sort()
        queue = deque([("", set())])
        curr_len = 0
        while queue:
            if curr_len == len(letters):
                return [tup[0] for tup in list(queue)]
            size = len(queue)
            for _ in range(size):
                combo, char_ind_set = queue.popleft()
                for i in range(len(letters)):
                    if i in char_ind_set:
                        continue
                    if i > 0 and letters[i] == letters[i - 1] and i - 1 not in char_ind_set:
                        continue
                    queue.append((combo + letters[i], char_ind_set | {i})) 
            curr_len += 1
            
            
# Using iterative DFS, implemented with a stack. Time to execute is longer than the recursive version.
# Unlike the BFS version, this one won't encounter space complexity issues.
class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        letters = [char for char in str]
        letters.sort()
        stack = [("", set())]
        permutations = []
        while stack:
            combo, selected_ind_set = stack.pop()
            if len(combo) == len(letters):
                permutations.append(combo)
                continue
            for i in range(len(letters)):
                if i in selected_ind_set:
                    continue
                if i > 0 and letters[i - 1] == letters[i] and i - 1 not in selected_ind_set:
                    continue
                stack.append((combo + letters[i], selected_ind_set | {i}))
        return permutations
    
    
# A slight modification of the above version. Instead of keeping a set of indices of selected characters in each
# element of the stack, we now keep a string of remaining letters to choose from. This solution is visibly faster
# than the one above, but still slightly slower than the recursive DFS version.
class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        letters = [char for char in str]
        letters.sort()
        stack = [("", letters)]
        permutations = []
        while stack:
            combo, remaining_letters = stack.pop()
            if len(combo) == len(letters):
                permutations.append(combo)
                continue
            for i in range(len(remaining_letters)):
                if i > 0 and remaining_letters[i - 1] == remaining_letters[i]:
                    continue
                stack.append((combo + remaining_letters[i], remaining_letters[:i] + remaining_letters[i + 1:]))
        return permutations
