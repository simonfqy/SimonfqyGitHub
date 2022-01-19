'''
Link: https://www.lintcode.com/problem/4/
'''

# My own solution. Actively constructs the ugly numbers rather than passively searching through natural numbers.
# Uses heap. Time complexity is O(nlogn).
import heapq
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        if n <= 0:
            return None
        ugly_numbers_set = set()
        min_heap = [1]
        prime_factors = [2, 3, 5]
        for i in range(n):
            curr_num = heapq.heappop(min_heap)
            if i == n - 1:
                return curr_num            
            for factor in prime_factors:
                new_num = curr_num * factor
                if new_num in ugly_numbers_set:
                    continue
                heapq.heappush(min_heap, new_num)
                ugly_numbers_set.add(new_num)
                
                
