'''
Link: https://www.lintcode.com/problem/10/
'''

# My own solution, recursive, using DFS.
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

