'''
Link: https://www.lintcode.com/problem/513/
'''


# My own solution. Uses some elements from BFS and dynamic programming.
from collections import deque
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        square_list = self.get_square_list(n)
        squares_set = set(square_list)
        if n in squares_set:
            return 1
        m = len(square_list)
        queue = deque([(square_list[i], i) for i in range(m)])
        for length in range(1, n + 1):
            size = len(queue)
            for _ in range(size):
                summ, last_ind = queue.popleft()
                if n - summ in squares_set:
                    return length + 1
                # Start from last_ind and don't visit smaller indices. Otherwise there'll be duplicates.
                for i in range(last_ind, m):
                    if summ + square_list[i] > n:
                        break
                    new_sum = summ + square_list[i]
                    queue.append((new_sum, i))

    def get_square_list(self, n):  
        square_list = []
        for i in range(1, n + 1):
            power = i ** 2
            if power > n:                
                break
            square_list.append(power)
        # Reverse the squares list so that the larger values appear first. If we don't reverse it, we'll encounter memory limit exceeded issue.
        # By having the larger values appear first, we'll reach the target sum (n) earlier than otherwise.
        square_list.reverse()
        return square_list

      
