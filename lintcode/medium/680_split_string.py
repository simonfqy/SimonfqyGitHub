'''
Link: https://www.lintcode.com/problem/680/
'''

# My own solution. Uses DFS. 
class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        results = self.split_string(0, len(s) - 1, s)
        if results == []:
            return [[]]
        return results

    # Returns the list of all the splitted strings in s[i : j + 1] 
    def split_string(self, start, end, s):
        results = []
        curr = ""
        for i in range(start, start + 2):
            if i > end:
                break
            curr += s[i]
            later_string_splits = self.split_string(i + 1, end, s)
            curr_list = [curr]
            # Note that when later_string_splits is empty (it happens when i + 1 > end),
            # we need to add curr_list to the results. Otherwise, the whole function will return [].
            if not later_string_splits:
                results.append(curr_list)
            for later_string in later_string_splits:                
                results.append(curr_list + later_string)
        return results
    
      
# My own solution, slightly improved upon the previous one, using DFS with memoization. 
class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        self.memo = dict()
        results = self.split_string(0, len(s) - 1, s)        
        if results == []:
            return [[]]
        return results

    # Returns the list of all the splitted strings in s[i : j + 1] 
    def split_string(self, start, end, s):
        if (start, end) in self.memo:
            return self.memo[(start, end)]
        results = []
        curr = ""
        for i in range(start, start + 2):
            if i > end:
                break
            curr += s[i]
            later_string_splits = self.split_string(i + 1, end, s)
            curr_list = [curr]
            # Note that when later_string_splits is empty (it happens when i + 1 > end),
            # we need to add curr_list to the results. Otherwise, the whole function will return [].
            if not later_string_splits:
                results.append(curr_list)
            for later_string in later_string_splits:                
                results.append(curr_list + later_string)
        self.memo[(start, end)] = results
        return results
    
    
# My own solution, uses DFS, this time without memoization. The results are written into a global
# variable self.results while traversing, so we can't use memoization.
class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        self.results = []
        self.split_string(0, len(s) - 1, s, []) 
        return self.results

    # Adds all the split strings of s[start : end + 1] into self.results.
    def split_string(self, start, end, s, list_under_construction):
        if start == len(s):
            self.results.append(list_under_construction)        
        curr = ""
        for i in range(start, start + 2):
            if i > end:
                break
            curr += s[i]            
            self.split_string(i + 1, end, s, list_under_construction + [curr])
            
            
# My solution based on the description of a Jiuzhang.com's student. It uses DP without DFS and is calculated iteratively.
# We only need to keep record of 2 arrays: 1 for the s[i + 1:], the other for s[i + 2:].
# The split strings for s[i:] can be constructed depending on only these 2.
class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """
    def splitString(self, s):
        # write your code here
        n = len(s)
        next_inds_split_strings = [[], []]
        result = [[]]
        for i in range(n - 1, -1, -1):
            if not next_inds_split_strings[1]:
                next_inds_split_strings[1].append([s[i]])
                result = list(next_inds_split_strings[1])
                continue
            if not next_inds_split_strings[0]:
                next_inds_split_strings[0].append([s[i : i + 2]])
                next_inds_split_strings[0].append([s[i], s[i + 1]])
                result = list(next_inds_split_strings[0])
                continue
            result = []
            for succeeding_ind_split_str in next_inds_split_strings[0]:
                result.append([s[i]] + succeeding_ind_split_str)
            for second_succeeding_ind_split_str in next_inds_split_strings[1]:
                result.append([s[i : i + 2]] + second_succeeding_ind_split_str)
            next_inds_split_strings[0], next_inds_split_strings[1] = result, next_inds_split_strings[0]
        
        return result
    
# The original DP solution from jiuzhang.com student, which my solution above is based upon.
# This solution is much more desirable than my solution above, next time we should use something like it. Having
# multiple statements in the beginning to handle edge cases is not a problem; compared to my solution above, it simplifies
# the code logic.
class Solution:
    """ Notice the similarities with fibonnaci
        solving in iterative ways
    """
    def splitString(self, s):        
        n = len(s)        
        if n == 0: return [[]]        
        if n == 1: return [[s[:]]] 
        # Yes, we can initialize n_2 with [[]], not [[s[n - 1]]]. This is a useful observation and can simplify the code.
        n_2, n_1 = [[]], [[s[n - 1]]]
        for i in range(2, n + 1):
            # We don't need to initialize n_0 outside of the for loop; it is guaranteed to enter this loop
            # and n_0 will always be initialized here.
            n_0 = []
            for sub in n_2:
                newSub = [s[n - i : n - i + 2]] + sub
                n_0.append(newSub)
            for sub in n_1:
                newSub = [s[n-i]] + sub
                n_0.append(newSub)                
            n_2, n_1 = n_1, n_0
            
        return n_0
