'''
https://www.lintcode.com/problem/198/
'''

# My own solution. Iterative, starting from the end. Took quite some effort to debug it.
# Time complexity should be O(n^2), if the hash set identity operation takes O(1). If it takes O(logn), it should be O(n^2 * logn). Space complexity is O(n).
# Normally the hash set identity operation takes O(1).
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
                    # A[j] can be equal to A[i]. This calculation gives the correct result whether A[j] equals A[i] or not.
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
    
# My own solution, slightly improved upon my first solution (but much more complicated) in that we don't need to compute
# factorial each time; instead, we calculate the factorial incrementally.
from collections import defaultdict
import math
class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndexII(self, A):
        order = 1
        num_to_occurrence = defaultdict(int)
        perm_count = 1
        num_to_factorial_of_occurrence = dict()
        num_to_occurrence[A[-1]] += 1
        num_to_factorial_of_occurrence[A[-1]] = 1
        for i in range(len(A) - 2, -1, -1):
            encountered_num = set()
            perm_count *= len(A) - 1 - i
            num_to_occurrence[A[i]] += 1
            if A[i] not in num_to_factorial_of_occurrence:
                num_to_factorial_of_occurrence[A[i]] = 1
            # Calculate the factorial incrementally
            num_to_factorial_of_occurrence[A[i]] *= num_to_occurrence[A[i]]
            smaller_count = 0
            divisor = 1
            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    smaller_count += 1
                if A[j] not in encountered_num:
                    divisor *= num_to_factorial_of_occurrence[A[j]]
                    encountered_num.add(A[j])
            order += smaller_count * perm_count / divisor
        return int(order) 
    
# Solution from jiuzhang.com. It is more optimized than my own solution. Fewer lines of code and better efficiency.   
class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndexII(self, A):
        order = 1
        num_to_occurrence = dict()
        divisor = 1
        perm_count = 1
        # Start from len(A) - 1, so we don't need to take care of A[-1] explicitly.
        for i in range(len(A) - 1, -1, -1):
            if A[i] not in num_to_occurrence:
                num_to_occurrence[A[i]] = 0
            num_to_occurrence[A[i]] += 1
            if num_to_occurrence[A[i]] > 1:
                # Uses the fact that we only need 1 divisor variable for all i's.
                # The divisor can be calculated incrementally rather than multiplying
                # by factorial explicitly. This decreases the amount of work in the j for loop.
                divisor *= num_to_occurrence[A[i]]
            smaller_count = 0
            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    smaller_count += 1
            
            order += perm_count * smaller_count // divisor
            # If we put it earlier in the for loop body, the calculation would be incorrect. 
            # If we use perm_count *= len(A) - 1 - i and put it earlier in the for loop body,
            # the value will become zero. So this way is appropriate.
            perm_count *= len(A) - i

        return order
