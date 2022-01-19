'''
Link: https://www.lintcode.com/problem/518
'''

# My own solution. Uses dynamic programming, has O(nk) time complexity and O(n) space complexity. This solution is basically copied from
# https://github.com/simonfqy/SimonfqyGitHub/blob/d9370febac2ec7aac65edf564abaa5887f2c2e21/lintcode/medium/4_ugly_number_ii.py#L52
class Solution:
    """
    @param n: a positive integer
    @param primes: the given prime list
    @return: the nth super ugly number
    """
    def nthSuperUglyNumber(self, n, primes):
        k = len(primes)
        pointers = [0] * k
        dp = [1] * n
        for i in range(1, n):
            candidates = []
            for j in range(k):
                candidates.append(dp[pointers[j]] * primes[j])
            dp[i] = min(candidates)
            for j in range(k):
                if candidates[j] == dp[i]:
                    pointers[j] += 1

        return dp[n - 1]

    
# My own solution. Uses heap, has O(nklognk) time complexity and O(nk) space complexity. This solution is basically copied from
# https://github.com/simonfqy/SimonfqyGitHub/blob/d9370febac2ec7aac65edf564abaa5887f2c2e21/lintcode/medium/4_ugly_number_ii.py#L33
import heapq
class Solution:
    """
    @param n: a positive integer
    @param primes: the given prime list
    @return: the nth super ugly number
    """
    def nthSuperUglyNumber(self, n, primes):
        min_heap = [(1, 1)]
        ugly_num = 1
        for _ in range(n):
            ugly_num, m = heapq.heappop(min_heap)
            for factor in primes:
                if factor < m:
                    continue
                heapq.heappush(min_heap, (ugly_num * factor, factor))
        return ugly_num
    

    
