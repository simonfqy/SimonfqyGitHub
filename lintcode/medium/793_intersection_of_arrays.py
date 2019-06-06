'''
Link: https://www.lintcode.com/problem/intersection-of-arrays/description
'''

# A straightforward Python solution by myself.
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        intersection_so_far = set()
        for i, arr in enumerate(arrs):
            if i == 0:
                intersection_so_far = set(arr)
                continue
            intersection_so_far.intersection_update(arr)
        return len(intersection_so_far)
