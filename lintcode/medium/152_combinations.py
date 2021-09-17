'''
Link: https://www.lintcode.com/problem/152/
'''

# My own solution, using DFS.
class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        start = 1
        combinations = []
        self.get_combinations(start, n, k, [], combinations)
        return combinations

    def get_combinations(self, start, n, k, combo_so_far, combinations):
        if len(combo_so_far) == k:
            combinations.append(combo_so_far)
            return
        for i in range(start, n + 1):
            self.get_combinations(i + 1, n, k, combo_so_far + [i], combinations)
            
            
# My own solution, using DFS. This time it is divide-and-conquer, so that we return partially-constructed
# combination in each recursive function call.
class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        start = 1
        return self.get_combinations(start, n, k)

    def get_combinations(self, start, n, k):        
        if k == 0:            
            return [[]]
        combinations = []
        for i in range(start, n + 1):
            suffix_combos = self.get_combinations(i + 1, n, k - 1)
            for combo in suffix_combos:
                combinations.append([i] + combo)
        return combinations

# Slightly improved upon the previous solution by adding memoization.
class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        start = 1
        self.memo = dict()
        return self.get_combinations(start, n, k)

    def get_combinations(self, start, n, k):        
        if k == 0:            
            return [[]]
        if (start, k) in self.memo:
            return self.memo[(start, k)]
        combinations = []
        for i in range(start, n + 1):
            suffix_combos = self.get_combinations(i + 1, n, k - 1)
            for combo in suffix_combos:
                combinations.append([i] + combo)
        self.memo[(start, k)] = combinations
        return combinations
