'''
https://www.lintcode.com/problem/135/
'''

# My own solution, recursive DFS.
# Time complexity: O(n^(target/min)), where n is the size of candidates, min is the smallest number among them. In each satisfying combination, each element
# has n choices, while there are at most target/min elements in each combination, so we have O(n^(target/min))。
# Space complexity: also O(n^(target/min)), because there are at most n^(target/min) distinct combinations in the list which stores the satisfying combinations.
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
        
        
# Solution from a student on jiuzhang.com. Uses BFS, not DFS.
from collections import deque
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        candidates.sort()
        results = []
        self.bfs(candidates, target, results)
        return results
        
    def bfs(self, candidates, target, results):
        q = deque([])
        for i in range(len(candidates)):
            # 去重
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            q.append([candidates[i]])
            
        while q:
            tmp = q.popleft()
            if sum(tmp) == target:
                results.append(tmp)
            for i in range(len(candidates)):
                # 去重 && 同时去掉比小于当前遍历的最后一个（也是最大）值，只取大于等于的那些
                if i > 0 and candidates[i] == candidates[i - 1] or candidates[i] < tmp[-1]:
                    continue
                if sum(tmp) + candidates[i] <= target:
                    list_in_q = tmp[:]
                    list_in_q.append(candidates[i])
                    q.append(list_in_q)
