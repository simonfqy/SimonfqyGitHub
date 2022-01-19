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
                
         
# A solution from a student on jiuzhang.com. Uses heap and has O(nlogn) time complexity, but does not need to use hashmap for deduplication,
# because the ascending order of prime factors is guaranteed when producing the ugly numbers. 
import heapq
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        min_heap = [(1, 1)]
        num = 1
        for _ in range(n):
            num, m = heapq.heappop(min_heap)
            for factor in [2, 3, 5]:
                if factor < m:
                    continue
                heapq.heappush(min_heap, (num * factor, factor))
        return num        
        
                
# My implementation based on the Dynamic Programming solution from jiuzhang.com. Uses pointers instead of heap, has O(n) time complexity. 
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # Index of the pointers
        # Intuition: the next ugly number must be constructed by *2, *3 or *5, so we can maintain pointers to the element producing the
        # current ugly number. dp[pointers[i]] * factors[i] where i = 0, 1, 2 are the only 3 candidates for the next ugly number. Hence,
        # we don't need to use a heap.
        pointers = [0, 0, 0]
        factors = [2, 3, 5]
        dp = [1] * n
        for i in range(1, n):
            triplet = (dp[pointers[0]] * factors[0], dp[pointers[1]] * factors[1], dp[pointers[2]] * factors[2])
            dp[i] = min(triplet)
            for j in range(3):
                if triplet[j] == dp[i]:
                    pointers[j] += 1   
                    # We cannot use break here; otherwise duplicates will be introduced, for example, 2 * 3 = 6 and 3 * 2 = 6.
                    # Need to increment the pointer for duplicates too.                 

        return dp[n - 1]
    

    
