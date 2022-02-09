'''
Link: https://www.lintcode.com/problem/116/
'''


# My own solution. Uses dynamic programming, has O(n^2) time complexity.
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        n = len(A)
        can_reach = [False] * n
        can_reach[0] = True
        for i in range(n):
            if not can_reach[i]:
                break
            max_jump_len = A[i]
            for j in range(i + 1, i + max_jump_len + 1):
                if j >= n:
                    break
                can_reach[j] = True
                if j == n - 1:
                    return True
        return can_reach[n - 1]


# My own solution. Uses greedy algorithm, has O(n) time complexity.
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        n = len(A)
        reachable_frontier = 0
        for i in range(n):
            if i > reachable_frontier:
                break
            reachable_frontier = max(reachable_frontier, i + A[i])
        return reachable_frontier >= n - 1
    
    
    
