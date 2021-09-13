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
    
# Also my own solution, uses DFS without memoization. Uses a global variable to store the paths. Takes longer time, but correct.
class Solution:
    """
    @param n: An integer
    @param str1: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str1):
        # write your code here
        self.path = []
        self.find_missing(n, str1, 0, len(str1) - 1, [])
        for i in range(1, n + 1):
            if i not in self.path[0]:
                return i
    
    def find_missing(self, n, str1, start, end, path_so_far):
        if start > end:
            self.path.append(path_so_far)
            return
        for i in range(start, end + 1):
            curr_num = int(str1[start : i + 1])
            if curr_num < 1 or curr_num > n:
                break
            if curr_num in path_so_far:
                continue
            self.find_missing(n, str1, i + 1, end, path_so_far + [curr_num])
            
# Uses dynamic programming. This is my own solution, but it is borrowed from the solution in 
# https://github.com/simonfqy/SimonfqyGitHub/blob/14d82e0b741162f52c343e967e067be62869f4c3/lintcode/medium/680_split_string.py#L137.
# It uses 2 transient variables to store the list of integers parsed for the prior digit and the digit prior to that one. It is because
# n < 100, so any numbers contained in the list must be no more than 2 digits.
class Solution:
    """
    @param n: An integer
    @param str1: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str1):
        # write your code here
        length = len(str1)
        if length == 0:
            return 1
        if length == 1:
            for i in range(1, n + 1):
                if i != int(str1):
                    return i
        if length == 2:
            a, b = int(str1[0]), int(str1[1])
            for i in range(1, n + 1):
                if i != a and i != b:
                    return i
        n_0, n_1 = [[]], [[int(str1[0])]]
        for i in range(1, length):
            n_2 = []
            one_digit = int(str1[i])
            two_digit = int(str1[i - 1 : i + 1]) 
            for num_list in n_1:
                if one_digit < 1 or one_digit > n:
                    break
                if one_digit in num_list:
                    continue
                n_2.append(num_list + [one_digit])
            for num_list in n_0:
                # one_digit == two_digit can filter out the situation where str1[i] is 0.
                if one_digit == two_digit or two_digit < 1 or two_digit > n:
                    break
                if two_digit in num_list:
                    continue
                n_2.append(num_list + [two_digit])
            n_0, n_1 = n_1, n_2
        for j in range(1, n+1):
            if j in n_2[0]:
                continue
            return j
        
        
# The answer from jiuzhang.com. Directly includes the find missing logic inside the recursive function
# as the base case.
class Solution:
    """
    @param n: An integer
    @param str1: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str1):
        # write your code here
        obtained = [False] * (n + 1)
        return self.find_missing(n, str1, 0, obtained)

    def find_missing(self, n, str1, start_ind, obtained):
        if start_ind >= len(str1):
            results = []
            for i in range(1, n + 1):
                if not obtained[i]:
                    results.append(i)
            if len(results) == 1:
                return results[0]
            return -1
        
        if str1[start_ind] == '0':
            return -1
        
        for length in range(1, 3):
            # Here we don't need to check for start_ind + length <= len(str1), because when
            # it doesn't satisfy this requirement, str1[start_ind : start_ind + length] will
            # simply return the last few characters in str1 and not throw errors.
            num = int(str1[start_ind : start_ind + length])
            if num < 1 or num > n or obtained[num]:
                continue
            obtained[num] = True
            res = self.find_missing(n, str1, start_ind + length, obtained)
            if res != -1:
                return res
            obtained[num] = False
        return -1
