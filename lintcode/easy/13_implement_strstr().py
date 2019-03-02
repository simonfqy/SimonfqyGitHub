'''
Link: https://www.lintcode.com/problem/implement-strstr/description
'''
# This is my own brute-force solution, which is O(n^2).
class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
       
        len_source = len(source)
        len_target = len(target)
        if len_source <= 0 and source == target:
            return 0
        for start_ind in range(len_source):
            sub = source[start_ind : start_ind + len_target]
            if sub == target:
                return start_ind
        return -1
