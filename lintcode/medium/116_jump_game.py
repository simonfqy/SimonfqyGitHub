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


