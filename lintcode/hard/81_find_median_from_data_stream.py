'''
Link: https://www.lintcode.com/problem/81/
'''

# This solution should be correct, but causes time limit exceeded exception.
class Solution:
    data = []
    """
    @param val: a num from the data stream.
    @return: nothing
    """
    def add(self, val: int):        
        first_greater_element_ind = self.get_first_greater_element_ind(val)
        self.data = self.data[:first_greater_element_ind] + [val] + self.data[first_greater_element_ind:]

    def get_first_greater_element_ind(self, val):
        if len(self.data) == 0:
            return 0
        left, right = 0, len(self.data) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if self.data[mid] <= val:
                left = mid
            else:
                right = mid
        if self.data[left] > val:
            return left
        if self.data[right] > val:
            return right
        return len(self.data)

    """
    @return: return the median of the all numbers
    """
    def getMedian(self) -> int:
        return self.data[(len(self.data) - 1) // 2]
