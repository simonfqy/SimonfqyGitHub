'''
Link: https://www.lintcode.com/problem/smallest-rectangle-enclosing-black-pixels/description
'''

# This is my own implementation. It is correct, but has a too high time complexity. It uses BFS.
from collections import deque
class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        if image is None or not len(image):
            return 0
        seen = set()
        queue = deque()
        queue.append((x, y))
        seen.add((x, y))
        max_x, max_y = 0, 0
        min_x, min_y = len(image) - 1, len(image[0]) - 1
        dxy = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while len(queue):
            node = queue.popleft()
            if node[0] < min_x:
                min_x = node[0]
            if node[0] > max_x:
                max_x = node[0]
            if node[1] < min_y:
                min_y = node[1]
            if node[1] > max_y:
                max_y = node[1]
            for d_xy in dxy:
                this_node = (d_xy[0] + node[0], d_xy[1] + node[1])
                if this_node[0] < 0 or this_node[0] >= len(image):
                    continue
                if this_node[1] < 0 or this_node[1] >= len(image[0]):
                    continue
                if this_node in seen:
                    continue
                if image[this_node[0]][this_node[1]] == '0':
                    continue
                seen.add(this_node)
                queue.append(this_node)
        return ((max_y - min_y + 1) * (max_x - min_x + 1))
    
# The solution based on the one given in Jiuzhang.com.
class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        if image is None or not len(image) or not len(image[0]) or image[0] is None:
            return 0
        
        start, end = 0, x
        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_row_black(image, mid):
                end = mid
            else:
                start = mid
        if self.is_row_black(image, start):
            first_row_ind = start
        elif self.is_row_black(image, end):
            first_row_ind = end
        
        start, end = x, len(image) - 1 
        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_row_black(image, mid):
                start = mid
            else:
                end = mid
        if self.is_row_black(image, end):
            last_row_ind = end
        elif self.is_row_black(image, start):
            last_row_ind = start
        
        start, end = 0, y
        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_col_black(image, mid):
                end = mid
            else:
                start = mid
        if self.is_col_black(image, start):
            first_col_ind = start
        elif self.is_col_black(image, end):
            first_col_ind = end
            
        start, end = y, len(image[0]) - 1 
        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_col_black(image, mid):
                start = mid
            else:
                end = mid
        if self.is_col_black(image, end):
            last_col_ind = end
        elif self.is_col_black(image, start):
            last_col_ind = start
        
        return (last_col_ind - first_col_ind + 1) * (last_row_ind - first_row_ind + 1)
    
    
    def is_row_black(self, image, row_num):
        for col in range(len(image[0])):
            if image[row_num][col] == '1':
                return True
        return False
    
    def is_col_black(self, image, col_num):
        for row in range(len(image)):
            if image[row][col_num] == '1':
                return True
        return False 
