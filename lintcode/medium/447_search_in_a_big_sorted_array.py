'''
Link: https://www.lintcode.com/problem/search-in-a-big-sorted-array/description
'''

# The following solution is my own.
"""
Definition of ArrayReader
class ArrayReader(object):
    def get(self, index):
    	# return the number on given index, 
        # return 2147483647 if the index is invalid.
"""
class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        if target is None or reader is None:
            return -1
        start = 0
        if target > 0:
            end = target - 1
        else:
            end = 0
        gap = max(target, 1)
        while reader.get(end) < target:
            start = end
            end += gap
            gap += gap
        while start + 1 < end:
            mid = (start + end) // 2
            if reader.get(mid) < target:
                start = mid
            else:
                end = mid
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
