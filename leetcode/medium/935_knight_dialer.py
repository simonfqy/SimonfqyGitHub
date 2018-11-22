"""Link: https://leetcode.com/problems/knight-dialer/
This solution comes from the discussion page. In my own implementation I could never make it within the time limit. The ingenuity
with this unconventional solution is that it uses the adjacency matrix. Adjacency matrix has an interesting property: 
If A is the adjacency matrix of the directed or undirected graph G, then the matrix A^n (i.e., the matrix product of n copies of A) 
has an interesting interpretation: the element (i, j) gives the number of (directed or undirected) walks of length n from vertex i 
to vertex j. If n is the smallest nonnegative integer, such that for some i, j, the element (i, j) of A^n is positive, then n is 
the distance between vertex i and vertex j.
TAKEAWAY: we might be able to take advantage of this property of adjacency matrix to solve problems related to the number of paths
between two nodes."""

import numpy as np
class Solution:
    def __init__(self):
        self.next_move_dict = {0: [4, 6], 1:[6, 8], 2:[7, 9], 3:[4, 8], 4:[3, 9, 0], 5:[],
                               6:[1, 7, 0], 7:[2, 6], 8:[1, 3], 9:[2, 4]}  
    
    def knightDialer(self, N):
        mod = 10**9 + 7
        #if N == 1: return 10
        M = np.matrix([[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                       [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]])
        res = np.matrix([[1]*10])
        N -= 1
        while N:
            if N % 2 != 0: 
                res = res * M % mod                
                N -= 1
            else:
                M = M * M % mod
                N /= 2
        return int(np.sum(res)) % mod
