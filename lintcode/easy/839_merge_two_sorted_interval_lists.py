'''
Link: https://www.lintcode.com/problem/839/
'''


# My own solution. Overrides the __lt__ function of Interval class. Has O(n) time complexity where n is the total number of intervals. 
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

Interval.__lt__ = lambda x, y: (x.start < y.start or (x.start == y.start and x.end < y.end))
class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        merged_list = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                candidate_next = list1[i]
                i += 1
            else:
                candidate_next = list2[j]
                j += 1
            self.add_candidate_next_interval(merged_list, candidate_next)
        for ind_1 in range(i, len(list1)):
            self.add_candidate_next_interval(merged_list, list1[ind_1])
        for ind_2 in range(j, len(list2)):
            self.add_candidate_next_interval(merged_list, list2[ind_2])
        return merged_list

    def add_candidate_next_interval(self, merged_list, candidate_next):
        if not merged_list:
            merged_list.append(candidate_next)
            return        
        last_interval = merged_list[-1]
        if last_interval.end < candidate_next.start:
            merged_list.append(candidate_next)
        elif last_interval.end < candidate_next.end:
            merged_list[-1].end = candidate_next.end
            
            
            
