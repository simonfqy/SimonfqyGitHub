'''
Link: https://www.lintcode.com/problem/pancake-sorting/description
'''

# It is similar to selection sorting.
class Solution:
    """
    @param array: an integer array
    @return: nothing
    """
    def pancakeSort(self, array):
        # Write your code here
        end = len(array) - 1
        while end >= 0:
            max_ind = self.find_max_ind(array, end)
            if max_ind != end:
                # Need reversal in this case.
                FlipTool.flip(array, max_ind)
                FlipTool.flip(array, end)
            end -= 1
        return
        
        
    def find_max_ind(self, array, end):
        max_val = array[0]
        max_ind = 0
        
        for i in range(end + 1):
            if array[i] > max_val:
                max_val = array[i]
                max_ind = i
        return max_ind
