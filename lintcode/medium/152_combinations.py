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
