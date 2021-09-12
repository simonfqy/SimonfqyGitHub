'''
https://www.lintcode.com/problem/570/
'''

# My solution. Uses memorized DFS.
class Solution:
    """
    @param n: An integer
    @param str1: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str1):
        # write your code here
        self.memo = dict()
        numbers_found = self.get_all_combos(n, str1, 0, len(str1) - 1)
        for i in range(1, n + 1):
            if i in numbers_found[0]:
                continue
            return i
    
    # Populate the self.memo dict and return the valid combinations.
    # It took me some work to realize this function already does what we want, we don't need to use the number of resulting elements 
    # (n - 1 in the beginning) in the list as a parameter: the check for ensuring 1 <= num <= n and disallowing duplicates already 
    # achieves it.
    def get_all_combos(self, n, str1, start, end):
        if start > end:
            return [[]]            
        if (start, end) in self.memo:
            return self.memo[(start, end)]        
        self.memo[(start, end)] = []
        for i in range(start, end + 1):
            curr_num = int(str1[start : i + 1])
            # This condition, together with the condition below to disallow duplicates, can make
            # sure that we get the desired number of integers in the self.memo[(0, len(s) - 1)][0]
            if curr_num < 1 or curr_num > n:
                break
            combos_in_suffix = self.get_all_combos(n, str1, i + 1, end)
            for combo in combos_in_suffix:
                # Disallow duplicates.
                if curr_num in combo:
                    continue
                self.memo[(start, end)].append([curr_num] + combo)
        return self.memo[(start, end)]
