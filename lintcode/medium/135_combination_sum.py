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
            
            
# My own solution, recursive DFS with memoization, divide-and-conquer.
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates.sort()
        self.memo = dict()
        return self.helper(candidates, 0, len(candidates) - 1, target)

    def helper(self, candidates, start, end, target):
        if target == 0:            
            return [[]]
        if (start, target) in self.memo:
            return self.memo[(start, target)]
        combinations = []
        for i in range(start, end + 1):
            curr_num = candidates[i]
            if curr_num > target:
                break
            if i > start and curr_num == candidates[i - 1]:
                continue
            suffix_combos = self.helper(candidates, i, end, target - curr_num)
            for combo in suffix_combos:
                combinations.append([curr_num] + combo)
        self.memo[(start, target)] = combinations
        return combinations
    
    
# Solution from jiuzhang.com. Different from but similar to my own solution. 
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates.sort()
        results = []
        self.helper(candidates, 0, target, results, [])
        return results
    
    def helper(self, candidates, start, target, results, combo_so_far):
        if target == 0:
            results.append(combo_so_far)
            return
        if start >= len(candidates) or target < 0:
            return
        
        # Do not select the current start element.
        self.helper(candidates, start + 1, target, results, combo_so_far)

        if start > 0 and candidates[start] == candidates[start - 1]:
            return

        # Select the current start element
        self.helper(candidates, start, target - candidates[start], results, combo_so_far + [candidates[start]])
