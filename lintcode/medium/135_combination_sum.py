'''
https://www.lintcode.com/problem/135/
'''

# My own solution, recursive DFS.
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates.sort()
        combos = []
        self.helper(candidates, 0, len(candidates) - 1, target, [], combos)
        return combos

    def helper(self, candidates, start, end, target, combo_so_far, combos):
        if target == 0:
            combos.append(combo_so_far)
            return
        for i in range(start, end + 1):
            curr_num = candidates[i]
            if curr_num > target:
                break
            # Skip duplicate elements to avoid having duplicate combinations in the end.
            if i > start and curr_num == candidates[i - 1]:
                continue
            self.helper(candidates, i, end, target - curr_num, combo_so_far + [curr_num], combos)
