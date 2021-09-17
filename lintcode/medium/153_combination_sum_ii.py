'''
Link: https://www.lintcode.com/problem/153/
'''

# My own solution. Use a global variable to store the combinations.
class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        num = sorted(num)
        n = len(num)
        self.combinations = []
        self.get_combinations(num, 0, n - 1, target, [])
        return self.combinations

    def get_combinations(self, num, start_ind, end_ind, target, combination_so_far):
        if sum(combination_so_far) == target:
            if combination_so_far not in self.combinations:
                self.combinations.append(combination_so_far)
            return
        for i in range(start_ind, end_ind + 1):
            this_num = num[i]
            if this_num + sum(combination_so_far) > target:
                # break instead of continue, because the num list is sorted and the next element will not be smaller.
                break
            self.get_combinations(num, i + 1, end_ind, target, combination_so_far + [this_num])
            
            
# My own solution. Does not use global variables. Instead of using DFS traversal, now it is divide-and-conquer,
# and the helper function returns result.
class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        num = sorted(num)
        n = len(num)
        return self.get_combinations(num, 0, n - 1, target)

    def get_combinations(self, num, start_ind, end_ind, target):
        if target == 0:
            return [[]]   
        combinations = []      
        for i in range(start_ind, end_ind + 1):
            this_num = num[i]
            if this_num > target:
                # break instead of continue, because the num list is sorted and the next element will not be smaller.
                break                
            suffix_combinations = self.get_combinations(num, i + 1, end_ind, target - this_num)
            if not suffix_combinations:
                continue
            for suffix_combo in suffix_combinations:
                complete_combo = [this_num] + suffix_combo
                if complete_combo in combinations:
                    continue
                combinations.append(complete_combo)
        return combinations
    
    
# Solution from jiuzhang.com, I modified it slightly. Here we have a couple small optimizations
# compared to my solutions above.
class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        num = sorted(num)
        n = len(num)
        combinations = []
        self.get_combinations(num, 0, n - 1, target, [], combinations)
        return combinations

    def get_combinations(self, num, start_ind, end_ind, target, combination_so_far, combinations):
        if target == 0:
            combinations.append(combination_so_far)
            return
        for i in range(start_ind, end_ind + 1):
            # Avoid having duplicate combinations in the final result. Hence we don't need the check for combination in combination_list.
            if i > start_ind and num[i] == num[i - 1]:
                continue
            if num[i] > target:
                break
            # Target is reduced in the next recursion level.
            self.get_combinations(num, i + 1, end_ind, target - num[i], combination_so_far + [num[i]], combinations)
