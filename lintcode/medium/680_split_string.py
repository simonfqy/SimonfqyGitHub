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
