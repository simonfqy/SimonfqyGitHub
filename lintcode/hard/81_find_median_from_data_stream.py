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
    
    
# This solution uses heap and should be correct, but also causes time limit exceeded exception.
import heapq
class Solution:
    def __init__(self):
        self.smaller_half_negative_heap, self.bigger_half_heap = [], []
        heapq.heapify(self.smaller_half_negative_heap)
        heapq.heapify(self.bigger_half_heap)

    """
    @param val: a num from the data stream.
    @return: nothing
    """
    def add(self, val: int):  
        if len(self.smaller_half_negative_heap) > len(self.bigger_half_heap):
            biggest_element_in_smaller_half = -heapq.nsmallest(1, self.smaller_half_negative_heap)[0]
            # We need to increment the self.bigger_half_heap.
            if val >= biggest_element_in_smaller_half:
                heapq.heappush(self.bigger_half_heap, val)
            else:
                largest_in_smaller_half = -heapq.heapreplace(self.smaller_half_negative_heap, -val)
                heapq.heappush(self.bigger_half_heap, largest_in_smaller_half)
        else:      
            if len(self.bigger_half_heap) > 0:
                smallest_element_in_larger_half = heapq.nsmallest(1, self.bigger_half_heap)[0]
            # Increment the self.smaller_half_negative_heap
            if len(self.smaller_half_negative_heap) == 0 or val <= smallest_element_in_larger_half:
                heapq.heappush(self.smaller_half_negative_heap, -val)
            else:
                smallest_in_larger_half = heapq.heappushpop(self.bigger_half_heap, val)
                heapq.heappush(self.smaller_half_negative_heap, -smallest_in_larger_half)

    """
    @return: return the median of the all numbers
    """
    def getMedian(self) -> int:
        return -heapq.nsmallest(1, self.smaller_half_negative_heap)[0]
    
    
# This solution is from jiuzhang.com. It is similar in idea to my solution above, but it is much simpler.
# And most importantly, it passes the test cases. 
# Lesson learned: use heap when needed; keep a standalone median variable to reduce the time complexity which
# might be associated to selecting min value in the heap used in the solution above.
import heapq
class Solution:
    def __init__(self):
        self.median = 0
        self.is_empty = True
        self.smaller_nums = []
        self.larger_nums = []
        
    def add(self, val):
        if self.is_empty:
            self.median = val
            self.is_empty = False
            return
        if val <= self.median:
            heapq.heappush(self.smaller_nums, -val)
        else:
            heapq.heappush(self.larger_nums, val)
        if len(self.larger_nums) > len(self.smaller_nums) + 1:
            heapq.heappush(self.smaller_nums, -self.median)
            self.median = heapq.heappop(self.larger_nums)
        elif len(self.larger_nums) < len(self.smaller_nums):
            heapq.heappush(self.larger_nums, self.median)
            self.median = -heapq.heappop(self.smaller_nums)

    def getMedian(self):
        return self.median


