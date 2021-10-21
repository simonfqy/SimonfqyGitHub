'''
https://www.lintcode.com/problem/sliding-window-median/description
'''

# This solution gives wrong answer. I don't know why.
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        n = len(nums)
        if n <= 0 or n < k or k <= 0:
            return []
        if k == 1:
            return nums
        res = [0] * (n - k + 1)
        if k == 2:
            for i in range(n - 1):
                res[i] = min(nums[i], nums[i + 1])
            return res
        sorted_nums = sorted(nums)
        
        window_elements = [0] * k
        for i in range(k):
            window_elements[i] = nums[i]
        window_elements.sort()
        mid_ind = (k - 1) // 2
        res[0] = window_elements[mid_ind]
        for i in range(1, n - k + 1):
            new_element = nums[i + k - 1]
            old_element = nums[i - 1]
            if new_element != old_element:
                window_elements.remove(old_element)
                self.insert_element(window_elements, new_element)
            res[i] = window_elements[mid_ind]
        return res
        
    
    def insert_element(self, ordered_list, new_element):
        place_to_insert = len(ordered_list)
        for ind, num in enumerate(ordered_list):
            if num > new_element:
                place_to_insert = ind
        ordered_list.insert(place_to_insert, new_element)
        return ordered_list
    
    
# This is my own solution, it uses heaps. It hits the time limit exceeded problem. Time complexity is O(nk), where n is the length of nums.
import heapq
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        if len(nums) == 0 or k == 0:
            return []
        smaller_nums, bigger_nums = [], []
        medians = []
        for start in range(len(nums) - k + 1):
            medians.append(self.get_median(nums, k, start, smaller_nums, bigger_nums))
        return medians

    def get_median(self, nums, k, start, smaller_nums, bigger_nums):
        end = start + k - 1 # It is inclusive
        if start == 0:
            sorted_section = sorted(nums[start : end + 1])
            for i in range((k - 1)//2, -1, -1):
                heapq.heappush(smaller_nums, -sorted_section[i])
            for i in range((k - 1)//2 + 1, k):
                heapq.heappush(bigger_nums, sorted_section[i])
            return -smaller_nums[0]
        
        curr_median = -smaller_nums[0]     
        # If we remove nums[start - 1] before pushing nums[end], we'll encounter exceptions saying that the element doesn't exist in the list. 
        # If we add a condition of `nums[start - 1] in set(bigger_nums)` after `nums[start - 1] > curr_median` in the if condition, 
        # it'll solve the problem, and we'll be able to remove nums[start - 1] before adding nums[end].
        if nums[end] > curr_median:
            heapq.heappush(bigger_nums, nums[end])
        else:
            heapq.heappush(smaller_nums, -nums[end])      
        if nums[start - 1] > curr_median:
            bigger_nums.remove(nums[start - 1])
            # Heapify after removing element is crucial, otherwise there will be nasty errors, because the list no longer satisfies heap requirements.
            # Whether we heapify the bigger_nums and smaller_nums right after declaring them won't make a difference.
            heapq.heapify(bigger_nums)
        else:
            smaller_nums.remove(-nums[start - 1])
            heapq.heapify(smaller_nums)            
        if len(bigger_nums) > len(smaller_nums):
            transfer = heapq.heappop(bigger_nums)
            heapq.heappush(smaller_nums, -transfer)
        elif len(smaller_nums) > len(bigger_nums) + 1:
            transfer = heapq.heappop(smaller_nums)
            heapq.heappush(bigger_nums, -transfer)                           

        return -smaller_nums[0]
    
    
# This is my implementation of a solution provided by a user from lintcode.com. It uses 2 heapq heaps to implement a 
# custom Heap class. The difficult problem of remove() is now solved by having a second heapq storing the elements to
# be removed, which are actually removed when calling the peek() and pop() functions. Time complexity is O(nlogk).
import heapq

class Heap:
    def __init__(self):
        self.__q1, self.__q2 = [], []
    
    def push(self, val):
        heapq.heappush(self.__q1, val)
    
    def remove(self, val):
        heapq.heappush(self.__q2, val)

    def peek(self):
        while len(self.__q2) > 0 and self.__q2[0] == self.__q1[0]:
            heapq.heappop(self.__q1)
            heapq.heappop(self.__q2)
        if len(self.__q1) > 0:
            return self.__q1[0]        

    def pop(self):
        while len(self.__q2) > 0 and self.__q2[0] == self.__q1[0]:
            heapq.heappop(self.__q1)
            heapq.heappop(self.__q2)
        if len(self.__q1) > 0:
            return heapq.heappop(self.__q1)

    def size(self):
        return len(self.__q1) - len(self.__q2)


class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        if k == 0 or not nums:
            return []
        smaller_nums_negative_heap = Heap()
        bigger_nums_positive_heap = Heap()
        medians = []
        for end in range(len(nums)):
            self.populate_median(nums, k, end, smaller_nums_negative_heap, bigger_nums_positive_heap, medians)
        return medians

    def populate_median(self, nums, k, end, smaller_nums_negative_heap, bigger_nums_positive_heap, medians):
        start = end - k + 1 # Inclusive
        if end == 0: # If we change this condition to start <= 0, we'll introduce bugs.
            smaller_nums_negative_heap.push(-nums[end])
        else:
            curr_median = -smaller_nums_negative_heap.peek()            
            if nums[end] <= curr_median:
                smaller_nums_negative_heap.push(-nums[end])
            else:
                bigger_nums_positive_heap.push(nums[end])
            if start > 0:
                if nums[start - 1] <= curr_median:
                    smaller_nums_negative_heap.remove(-nums[start - 1])
                else:
                    bigger_nums_positive_heap.remove(nums[start - 1])

        if smaller_nums_negative_heap.size() < bigger_nums_positive_heap.size():
            transfer = bigger_nums_positive_heap.pop()
            smaller_nums_negative_heap.push(-transfer)
        elif smaller_nums_negative_heap.size() > bigger_nums_positive_heap.size() + 1:            
            transfer = -smaller_nums_negative_heap.pop()
            bigger_nums_positive_heap.push(transfer)
        if start >= 0:
            medians.append(-smaller_nums_negative_heap.peek())
        
