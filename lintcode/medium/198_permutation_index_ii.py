'''
https://www.lintcode.com/problem/198/
'''

# My own solution. Took quite some effort to debug it.
from collections import defaultdict
import math
class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndexII(self, A):
        order = 1
        permutation_count = 1
        d = defaultdict(int)
        d[A[-1]] += 1
        for i in range(len(A) - 2, -1, -1):
            smaller_count = 0
            permutation_count *= len(A) - 1 - i
            divisor = 1
            encountered_num = set()
            d[A[i]] += 1
            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    smaller_count += 1
                if A[j] not in encountered_num:
                    divisor *= math.factorial(d[A[j]])
                    encountered_num.add(A[j])
            order += smaller_count * permutation_count / divisor            

        return int(order)
