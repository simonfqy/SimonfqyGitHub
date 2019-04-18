'''
Link: https://www.lintcode.com/problem/sort-colors-ii/description
This problem can be trivially solved using counting sort or custom-implemented comparison-based sorting
algorithms. To achieve O(1) extra memory with the lowest possible time complexity, we can think it this way:
Instead of having log(n) layers of recursion resulting in O(nlogn) time complexity, we can use the fact
that k <= n and recurse based on both n and k, resulting in log(k) layers of recursion and O(nlogk) time 
complexity. This line of thinking is truly helpful. To do so, we need to set both the range of indices in
the recursion parameter passing, and the range of color codes in the parameter passing.

This solution is from the hint given by Jiuzhang.com. I was unable to come up with it on my own.
'''

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        if not colors or len(colors) <= 0 or k < 1:
            return
        left, right = 0, len(colors) - 1
        self.quicker_sort(colors, 1, k, left, right)
        
        
    def quicker_sort(self, colors, start_color, end_color, left_ind, right_ind):
        if right_ind <= left_ind or start_color >= end_color:
            return
        pivot = (start_color + end_color) // 2
        left, right = left_ind, right_ind
        while left <= right:
            while left <= right and colors[left] < pivot:
                left += 1
            while left <= right and colors[right] > pivot:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
        # This can avoid infinite loop.      
        if left_ind == left or right_ind == right:
            return
        
        self.quicker_sort(colors, start_color, pivot, left_ind, right)
        self.quicker_sort(colors, pivot, end_color, left, right_ind)
