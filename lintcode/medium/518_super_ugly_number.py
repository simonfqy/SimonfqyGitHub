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

    
