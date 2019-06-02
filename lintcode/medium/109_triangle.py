'''
Link: https://www.lintcode.com/problem/triangle/description
'''

# Correct, but causes time limit exceeded problem.
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        return self.minimum_triang(triangle, 0, 0)
        
    def minimum_triang(self, triangle, start_row, start_ind):
        if start_row >= len(triangle):
            return 0
        left_min = self.minimum_triang(triangle, start_row + 1, start_ind)
        right_min = self.minimum_triang(triangle, start_row + 1, start_ind + 1)
        return triangle[start_row][start_ind] + min(left_min, right_min)


# Correct but also exceeds time limit.
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        if len(triangle) <= 0:
            return None
        # Stack of coordinates of points.
        stack = [[0, 0]]
        node_values_on_the_path = []
        current_best = None
        current_sum = 0
        while stack:
            row, col = stack.pop()
            while row <= len(node_values_on_the_path) - 1:
                val_of_popped_node = node_values_on_the_path.pop()
                current_sum -= val_of_popped_node
            node_values_on_the_path.append(triangle[row][col])
            current_sum += triangle[row][col]
            if row == len(triangle) - 1:
                if current_best is None or current_sum < current_best:
                    current_best = current_sum
            else:
                stack.append([row + 1, col + 1])
                stack.append([row + 1, col])
        return current_best
    
    
