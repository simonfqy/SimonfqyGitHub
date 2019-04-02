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
