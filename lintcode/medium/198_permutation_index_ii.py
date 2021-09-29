'''
https://www.lintcode.com/problem/198/
'''

# My own solution. Iterative, starting from the end. Took quite some effort to debug it.
# Time complexity should be O(n^3). Space complexity is O(n).
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
            # At first I placed this increment statement at the end of the outer loop and caused bugs. That's because I didn't 
            # consider the case where A[i] is not unique in A[i:]. When analyzing the problems, we should come up with more 
            # comprehensive cases to understand it better.
            d[A[i]] += 1
            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    smaller_count += 1
                if A[j] not in encountered_num:
                    divisor *= math.factorial(d[A[j]])
                    encountered_num.add(A[j])
            order += smaller_count * permutation_count / divisor            

        return int(order)
    
# Also my own solution, essentially the same as the one above. Slightly more time intensive, because we calculate the factorial
# for each i, instead of multiplying the permutation_count by (len(A) - 1 - i) for each i.
from collections import defaultdict
import math
class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndexII(self, A):
        num_to_occurrence = defaultdict(int)
        for num in A:
            num_to_occurrence[num] += 1
        order = 1
        for i in range(len(A) - 1):
            encountered_num = set()
            smaller_count = 0
            order_multiplier = math.factorial(len(A) - 1 - i)
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    smaller_count += 1
                if A[j] not in encountered_num:
                    encountered_num.add(A[j])
                    order_multiplier /= math.factorial(num_to_occurrence[A[j]])
            order += smaller_count * order_multiplier
            num_to_occurrence[A[i]] -= 1
        return int(order)
