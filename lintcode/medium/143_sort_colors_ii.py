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
        
        
# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        self.sort(colors, 1, k, 0, len(colors) - 1)
        
    def sort(self, colors, color_from, color_to, index_from, index_to):
        if color_from == color_to or index_from == index_to:
            return
            
        color = (color_from + color_to) // 2
        
        left, right = index_from, index_to
        while left <= right:
            while left <= right and colors[left] <= color:
                left += 1
            while left <= right and colors[right] > color:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
        
        self.sort(colors, color_from, color, index_from, right)
        self.sort(colors, color + 1, color_to, left, index_to)
        

# According to the students, this version is also correct:
def sortColors2(self, colors, k):
    # write your code here
    self.rainbowSort(1, k, 0, len(colors) - 1, colors)

def rainbowSort(self, color_start, color_end, start, end, colors):
    if color_start >= color_end or start >= end:
        return

    pivot = (color_start + color_end) // 2 + 1
    left = start
    right = end

    while left <= right:
        while left <= right and colors[left] < pivot:
            left += 1
        while left <= right and colors[right] >= pivot:
            right -= 1
        if left <= right:
            colors[left], colors[right] = colors[right], colors[left]
            left += 1
            right -= 1

    self.rainbowSort(color_start, pivot - 1, start, right, colors)
    self.rainbowSort(pivot, color_end, left, end, colors)
